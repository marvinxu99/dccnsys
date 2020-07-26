# Generated by Django 3.0.8 on 2020-07-26 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chair_mail', '0001_initial'),
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='systemnotification',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='conferences.Conference'),
        ),
        migrations.AddField(
            model_name='groupmessage',
            name='conference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_group_emails', to='conferences.Conference'),
        ),
    ]
