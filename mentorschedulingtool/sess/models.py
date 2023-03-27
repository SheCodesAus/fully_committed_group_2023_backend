from django.db import models

# from mentors.models import Mentor 


class Session(models.Model):
    session_name = models.CharField(max_length=255)
    mentors_required = models.IntegerField()

    # mentors_assigned = models.IntegerField()

    # counts the number of mentors assigned to this session
    @property
    def mentors_assigned(self):
        return self.mentors.all().count()
    
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
    # project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    # mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, default=None)
    #TODO: ASSIGN A PROJECT TO THIS SESSION
    #TODO: DISPLAY THE LIST OF MENTORS THIS SESSION IS ASSIGNED TO
    #BUG: Circular reference issue. Revisit Crowdfunding backend for help

    # mentors = models.ManyToManyField(
    #     Mentor, related_name="sessions", blank=True
    #     )

    # Return the name of the session
    def __str__(self):

        return self.session_name