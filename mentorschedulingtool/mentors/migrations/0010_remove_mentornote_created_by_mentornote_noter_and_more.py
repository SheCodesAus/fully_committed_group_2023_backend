# Generated by Django 4.0.2 on 2023-04-02 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentors', '0009_mentornote_mentor_alter_mentornote_created_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mentornote',
            name='created_by',
        ),
        migrations.AddField(
            model_name='mentornote',
            name='noter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='noter_notes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='feedback',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='mentornote',
            name='mentor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='mentornotes', to='mentors.mentor'),
        ),
    ]
