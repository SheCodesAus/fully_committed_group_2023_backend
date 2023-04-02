from django.db import models

# from mentors.models import Mentor 
from programs.models import Program 

class Session(models.Model):

    # choice field options
    MODULE_TYPE_CHOICES = (
        ('html_css', 'HTML/CSS'),
        ('python', 'Python'),
        ('javascript_react', 'JavaScript/React'),
        ('django', 'Django'),
        ('drf', 'DRF'),
        ('group', 'Group'),
        ('one_day_workshop', 'One Day Workshop'),
        ('n/a', 'Not Applicable')
    )
    CITY_CHOICES = (
        ('Brisbane', 'Brisbane'),
        ('Sydney', 'Sydney'),
        ('Perth', 'Perth')
    )

    # session details
    session_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    city = models.CharField(max_length=255, choices=CITY_CHOICES)
    module_type = models.CharField(max_length=255, choices=MODULE_TYPE_CHOICES)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="sessions")

    # mentor counts
    junior_mentors_required = models.IntegerField(default=0)
    industry_mentors_required = models.IntegerField(default=0)
    lead_mentors_required = models.IntegerField(default=1)

    # counts the total number of mentors assigned to this session
    @property
    def total_mentors_assigned(self):
        return self.mentors.all().count()
    
    # counts the total number of mentors required for this session
    @property
    def total_mentors_required(self):
        return sum((self.junior_mentors_required, self.industry_mentors_required, self.lead_mentors_required))
    
    # Return the name of the session
    def __str__(self):
        return self.session_name

# uses the mentor model above to create a connection between mentor type and session
# this allows the mentor to be matched to the correct session / mentor type combination
# TODO: create junior/industry/lead mentors assigned fields in session
# TODO: create calc that sums the total in total_assigned_mentors
class SelectSession(models.Model):

    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name="selections")
    MENTOR_TYPE_CHOICES = [
        ('junior_mentor', 'Junior Mentor'),
        ('industry_mentor', 'Industry Mentor'),
        ('lead_mentor', 'Lead Mentor')
    ]
    mentor_type = models.CharField(max_length=255, choices=MENTOR_TYPE_CHOICES)
