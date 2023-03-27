from django.db import models

from mentors.models import Mentor 

# Create your models here.
class Session(models.Model):
    id = models.IntegerField(primary_key=True)
    session_name = models.CharField(max_length=255)
    mentors_required = models.IntegerField()

    mentors_assigned = models.IntegerField()

    # counts the number of mentors assigned to this session
    # @property
    # def mentors_assigned(self):
    #     return self.mentors.count()
    
    date = models.DateTimeField()
    CITY_CHOICES = (
        ('Brisbane', 'Brisbane'),
        ('Sydney', 'Sydney'),
        ('Perth', 'Perth')
    )
    city = models.CharField(max_length=255, choices=CITY_CHOICES)
    MODULE_TYPE_CHOICES = (
        ('html_css', 'HTML/CSS'),
        ('python', 'Python'),
        ('javascript_react', 'JavaScript/React'),
        ('django', 'Django'),
        ('drf', 'DRF'),
        ('group', 'Group'),
        ('one_day_workshop', 'One Day Workshop')
    )
    module_type = models.CharField(max_length=255, choices=MODULE_TYPE_CHOICES)

    #FK
    # program_id = models.ManyToManyField(Program, related_name="program")
    # mentor_id = models.ForeignKey(Mentor, on_delete=models.PROTECT, related_name="mentors")