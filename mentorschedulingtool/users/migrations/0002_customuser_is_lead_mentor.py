# Generated by Django 4.0.2 on 2023-04-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_lead_mentor',
            field=models.BooleanField(default=False),
        ),
    ]