# Generated by Django 4.0.2 on 2023-04-03 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sess', '0009_remove_session_date_session_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='end_date',
            new_name='end_day',
        ),
    ]