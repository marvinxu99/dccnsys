# Generated by Django 2.2.4 on 2019-09-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_artifact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artifact',
            options={'ordering': ['descriptor_id']},
        ),
    ]
