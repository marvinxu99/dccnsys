# Generated by Django 3.0.8 on 2020-07-26 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chair_mail', '0002_auto_20200725_2215'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conferences', '0001_initial'),
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupmessage',
            name='sent_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_group_emails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emailsettings',
            name='conference',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='email_settings', to='conferences.Conference'),
        ),
        migrations.AddField(
            model_name='emailsettings',
            name='frame',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chair_mail.EmailFrame'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='group_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='chair_mail.GroupMessage'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='sent_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_emails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='emailframe',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.Conference'),
        ),
        migrations.AddField(
            model_name='emailframe',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='recipients',
            field=models.ManyToManyField(related_name='group_emails', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='systemnotification',
            constraint=models.UniqueConstraint(fields=('conference', 'name'), name='unique_name'),
        ),
        migrations.AddField(
            model_name='submissionmessage',
            name='recipients',
            field=models.ManyToManyField(related_name='group_emails', to='submissions.Submission'),
        ),
    ]