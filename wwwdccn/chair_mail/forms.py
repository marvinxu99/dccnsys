from django import forms
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.template import Template, Context
from django.utils import timezone
from html2text import html2text
from markdown import markdown

from chair_mail.context import get_conference_context, get_user_context, \
    get_submission_context
from chair_mail.mailing_lists import find_list
from submissions.models import Submission
from users.models import User
from .models import EmailFrame, MSG_TYPE_USER


def parse_mailing_lists(names_string, separator=','):
    names = names_string.split(separator)
    names = [name for name in names if name.strip()]
    return [find_list(name) for name in names]


def parse_users(pks_string, separator=','):
    pks = set(map(lambda s: int(s), pks_string.split(separator)))
    return User.objects.filter(pk__in=pks)


class EmailFrameUpdateForm(forms.ModelForm):
    class Meta:
        model = EmailFrame
        fields = ('text_html', 'text_plain')

    def save(self, commit=True):
        template = super().save(commit=False)
        template.updated_at = timezone.now()
        if commit:
            template.save()
        return template


class EmailFrameTestForm(forms.Form):
    text_html = forms.CharField(widget=forms.Textarea())
    text_plain = forms.CharField(widget=forms.Textarea())

    def send_message(self, user, conference):
        body_html = f"<p>Dear {user.profile.get_full_name()},</p>" \
            f"<p>this is a test generated by the registration system.</p>"
        body_plain = html2text(body_html)
        subject = 'Template test'

        html = EmailFrame.render(
            self.cleaned_data['text_html'], conference, subject, body_html
        )
        plain = EmailFrame.render(
            self.cleaned_data['text_plain'], conference, subject, body_plain
        )

        send_mail(
            subject=f'[{conference.short_name}] {subject}',
            message=plain,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message=html,
        )


class MessageForm(forms.Form):
    subject = forms.CharField()
    body = forms.CharField(widget=forms.Textarea(), required=False)
    lists = forms.CharField(
        required=False, max_length=1000, widget=forms.HiddenInput)

    def __init__(self, *args, msg_type=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg_type = msg_type
        self.cleaned_lists = []

    def clean_lists(self):
        _lists = parse_mailing_lists(self.cleaned_data['lists'])
        for ml in _lists:
            if ml.type != self.msg_type:
                raise ValidationError(
                    f'unexpected {ml.type} mailing list {ml.name}')
        self.cleaned_lists = _lists
        return self.cleaned_data['lists']


class UserMessageForm(MessageForm):
    users = forms.CharField(
        required=False, max_length=10000, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, msg_type=MSG_TYPE_USER, **kwargs)
        self.cleaned_users = []

    def clean_users(self):
        self.cleaned_users = list(parse_users(self.cleaned_data['users']))
        return self.cleaned_data['users']


class PreviewFormBase(forms.Form):
    subject = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'hidden': True
        })
    )

    body = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={
            'hidden': True
        })
    )

    def get_context(self, conference):
        raise NotImplementedError

    def render_html(self, conference):
        ctx_data = self.get_context(conference)
        context = Context(ctx_data, autoescape=False)
        subject_template = Template(self.cleaned_data['subject'])
        body_template = Template(self.cleaned_data['body'])
        subject = subject_template.render(context)
        body = markdown(body_template.render(context))
        return {
            'body': body,
            'subject': subject
        }


class PreviewUserMessageForm(PreviewFormBase):
    user = forms.CharField()  # Use simple CharField instead of choice!

    def get_context(self, conference):
        user = User.objects.get(pk=self.cleaned_data['user'])
        return {
            **get_conference_context(conference),
            **get_user_context(user, conference),
        }


class PreviewSubmissionMessageForm(PreviewFormBase):
    submission = forms.ChoiceField()
    user = forms.ChoiceField()

    def __init__(self, *args, submissions=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['submission'].choices = [
            (sub.pk, sub.title) for sub in submissions
        ]
        if len(submissions) == 1:
            self.fields['submission'].widget.attrs['hidden'] = True
        first_submission_users = [
            author.user for author in submissions[0].authors.all()
        ]
        self.fields['user'].choices = [
            (u.pk, u.profile.get_full_name()) for u in first_submission_users
        ]

    def get_context(self, conference):
        submission = Submission.objects.get(pk=self.cleaned_data['submission'])
        user = User.objects.get(pk=self.cleaned_data['user'])
        return {
            **get_conference_context(conference),
            **get_submission_context(submission),
            **get_user_context(user, conference),
        }