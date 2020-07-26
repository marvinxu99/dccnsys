# Generated by Django 3.0.8 on 2020-07-26 05:15

from django.db import migrations, models
import django.db.models.deletion
import submissions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, upload_to=submissions.models.get_attachment_full_path)),
                ('access', models.CharField(choices=[('NO', 'Inactive (no access)'), ('RO', 'Read only'), ('RW', 'Read and write')], default='RW', max_length=2)),
                ('code', models.CharField(blank=True, default='', max_length=32)),
                ('name', models.CharField(blank=True, default='', max_length=256)),
                ('label', models.CharField(blank=True, default='', max_length=256)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=250, verbose_name='Title')),
                ('abstract', models.CharField(default='', max_length=2500, verbose_name='Abstract')),
                ('status', models.CharField(choices=[('SUBMIT', 'Submitted'), ('REVIEW', 'Review'), ('REJECT', 'Rejected'), ('ACCEPT', 'Accepted'), ('PRINT', 'In-print'), ('PUBLISH', 'Published')], default='SUBMIT', max_length=10)),
                ('review_manuscript', models.FileField(blank=True, upload_to=submissions.models.get_review_manuscript_full_path)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('reached_overview', models.BooleanField(default=False)),
                ('filled_details', models.BooleanField(default=False)),
                ('conference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='conferences.Conference')),
            ],
        ),
    ]
