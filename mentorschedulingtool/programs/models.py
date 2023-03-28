from django.db import models

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
    # sum_mentors_required = models.IntegerField()
    # sum_mentors_assigned = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    city = models.CharField(max_length=50, choices=CITIES)
    program_type = models.CharField(max_length=50, choices=PROGRAM_TYPES)
    # session_id = models.IntegerField()