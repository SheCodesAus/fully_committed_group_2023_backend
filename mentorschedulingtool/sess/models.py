from django.db import models

# from mentors.models import Mentor 
from programs.models import Program 

class Session(models.Model):
    session_name = models.CharField(max_length=255)
    mentors_required = models.IntegerField()

    # counts the number of mentors assigned to this session
    @property
    def mentors_assigned(self):
        return self.mentors.all().count()
    # check if all is needed?
    
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
    
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="sessions")

    # Return the name of the session
    def __str__(self):

        return self.session_name