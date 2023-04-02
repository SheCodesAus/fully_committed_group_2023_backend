# from django.contrib.auth import get_user_model
from django.db import models
# from django.db.models import Sum, Count

# User = get_user_model()  # added to use the user

# Create your models here.
class Program(models.Model):
    PROGRAM_TYPES = (
        ('Plus', 'Plus'),
        ('Flash', 'Flash'),
        ('Workshop', 'Workshop')
    )
    CITIES = (
        ('Brisbane', 'Brisbane'),
        ('Sydney', 'Sydney'),
        ('Perth', 'Perth')
    )
    program_name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city = models.CharField(max_length=50, choices=CITIES)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPES)
    
    total_junior_mentors_required = models.IntegerField(default=0)
    total_industry_mentors_required = models.IntegerField(default=0)
    total_lead_mentors_required = models.IntegerField(default=0)

    total_mentors_required = models.IntegerField(default=0)
    total_mentors_assigned = models.IntegerField(default=0)

    # for loop: for each value in total_mentors_required on the sessions list, add to the sum of total_mentors_required
    @property
    def total_mentors_required(self):
        return sum(session.total_mentors_required for session in self.sessions.all())

    # for loop: for each value in total_mentors_assigned on the sessions list, add to the sum of total_mentors_assigned
    @property
    def total_mentors_assigned(self):
        return sum(session.total_mentors_assigned for session in self.sessions.all())
    
    # for loop: for each value in junior_mentors_required on the sessions list, add to the sum of total_junior_mentors_required
    @property
    def total_junior_mentors_required(self):
        return sum(session.junior_mentors_required for session in self.sessions.all())
    
    # for loop: for each value in industry_mentors_required on the sessions list, add to the sum of total_industry_mentors_required
    @property
    def total_industry_mentors_required(self):
        return sum(session.industry_mentors_required for session in self.sessions.all())

    # for loop: for each value in lead_mentors_required on the sessions list, add to the sum of total_lead_mentors_required
    @property
    def total_lead_mentors_required(self):
        return sum(session.lead_mentors_required for session in self.sessions.all())
