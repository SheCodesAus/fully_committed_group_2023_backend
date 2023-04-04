# Generated by Django 4.0.2 on 2023-04-02 00:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mentors', '0007_alter_mentor_sessions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MentorNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('notes_type', models.CharField(choices=[('Feedback', 'Feedback'), ('Case Note', 'Case Note'), ('Lead Mentor Suitability', 'Lead Mentor Suitability')], max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor_notes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
