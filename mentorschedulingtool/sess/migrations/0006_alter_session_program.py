# Generated by Django 4.0.2 on 2023-03-28 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0001_initial'),
        ('sess', '0005_session_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='program',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sessions', to='programs.program'),
        ),
    ]
