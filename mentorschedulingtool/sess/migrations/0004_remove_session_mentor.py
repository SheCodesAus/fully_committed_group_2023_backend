# Generated by Django 4.0.2 on 2023-03-27 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sess', '0003_session_mentor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='mentor',
        ),
    ]