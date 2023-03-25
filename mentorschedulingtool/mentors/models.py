from django.db import models

# Create your models here.
class Mentor(models.Model):
    html_css = 'html_css'
    python = 'python'
    javascript = 'javascript'
    react = 'react'
    django = 'django'
    drf = 'drf'
    SKILL_CHOICES = [
        (html_css, 'HTML/CSS'),
        (python, 'Python'),
        (javascript, 'JavaScript'),
        (react, 'React'),
        (django, 'Django'),
        (drf, 'DRF')
    ]

    Brisbane = 'Brisbane'
    Sydney = 'Sydney'
    Perth = 'Perth'
    CITY_CHOICES = [
        (Brisbane, 'Brisbane'),
        (Sydney, 'Sydney'),
        (Perth, 'Perth')
    ]

    STEP_CHOICES = [
        ('step_1_interview', 'Step 1 - Interview'),
        ('step_2_send_offer', 'Step 2 - Send Offer'),
        ('step_3_send_contract', 'Step 3 - Send Contract'),
        ('step_4_returned_contract', 'Step 4 - Returned Contract'),
        ('step_5_send_calendar_invite', 'Step 5 - Send Calendar Invite'),
        ('step_6_onboard_mentor', 'Step 6 - Onboard Mentor'),
        ('step_7_mentoring', 'Step 7 - Mentoring'),
        ('step_8_feedback_sent', 'Step 8 - Feedback Sent'),
        ('step_9_offboard_mentor', 'Step 9 - Offboard Mentor')
    ]

    PAID = 'paid'
    VOLUNTEER = 'volunteer'
    MENTOR_GIVE_BACK = 'mentor_give_back'
    PAYMENT_TYPE_CHOICES = [
        (PAID, 'Paid'),
        (VOLUNTEER, 'Volunteer'),
        (MENTOR_GIVE_BACK, 'Mentor Give Back')
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    will_travel = models.BooleanField()
    junior_mentor = models.BooleanField()
    industry_mentor = models.BooleanField()
    lead_mentor = models.BooleanField()
    she_codes_alumni = models.BooleanField()

    # need to select more than one
    skills = models.CharField(max_length=255, choices=SKILL_CHOICES)
    city = models.CharField(max_length=255, choices=CITY_CHOICES)
    current_step = models.CharField(max_length=255, choices=STEP_CHOICES)
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPE_CHOICES)
    notes = models.TextField()
    feedback = models.TextField()
    is_active = models.BooleanField()

    # FK to do
    module_id = models.IntegerField()
    program_id = models.IntegerField()

