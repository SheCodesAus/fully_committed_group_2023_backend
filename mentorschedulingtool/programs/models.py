from django.db import models
# from django.db.models import Sum, Count

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
    
    mentors_required = models.IntegerField(default=0)
    mentors_assigned = models.IntegerField(default=0)

    # for loop: for each value in mentors_required on the sessions list, add to the sum of mentors_required
    @property
    def mentors_required(self):
        return sum(session.mentors_required for session in self.sessions.all())

    # for loop: for each value in mentors_assigned on the sessions list, add to the sum of mentors_assigned
    @property
    def mentors_assigned(self):
        return sum(session.mentors_assigned for session in self.sessions.all())