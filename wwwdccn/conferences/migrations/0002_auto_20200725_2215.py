# Generated by Django 3.0.8 on 2020-07-26 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='chairs',
            field=models.ManyToManyField(related_name='chaired_conferences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='conference',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_conferences', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artifactdescriptorlink',
            name='descriptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='links', to='conferences.ArtifactDescriptor'),
        ),
        migrations.AddField(
            model_name='artifactdescriptorlink',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conferences.ExternalFile'),
        ),
        migrations.AddField(
            model_name='artifactdescriptor',
            name='proc_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artifacts', to='conferences.ProceedingType'),
        ),
        migrations.AlterUniqueTogether(
            name='artifactdescriptorlink',
            unique_together={('descriptor', 'link')},
        ),
    ]