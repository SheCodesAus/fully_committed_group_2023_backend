# Generated by Django 4.0.2 on 2023-03-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('session_name', models.CharField(max_length=255)),
                ('mentors_required', models.IntegerField()),
                ('mentors_assigned', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('city', models.CharField(choices=[('Brisbane', 'Brisbane'), ('Sydney', 'Sydney'), ('Perth', 'Perth')], max_length=255)),
                ('module_type', models.CharField(choices=[('html_css', 'HTML/CSS'), ('python', 'Python'), ('javascript_react', 'JavaScript/React'), ('django', 'Django'), ('drf', 'DRF'), ('group', 'Group'), ('one_day_workshop', 'One Day Workshop')], max_length=255)),
            ],
        ),
    ]
