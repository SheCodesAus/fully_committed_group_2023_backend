from django.db import models


from sess.models import Session
# Create your models here.
class Mentor(models.Model):
    Brisbane = 'Brisbane'
    Sydney = 'Sydney'
    Perth = 'Perth'
    CITY_CHOICES = [
        (Brisbane, 'Brisbane'),
        (Sydney, 'Sydney'),
        (Perth, 'Perth')
    ]

    STEP_CHOICES = [
        ('step_0_expression_of_interest_sent', 'Expression of Interest Sent'),
        ('step_0a_expression_of_interest_received', 'Expression of Interest Received'),
        
        ('step_1_interview_required', 'Step 1 - Interview Required'),
        ('step_1a_interview_not_required', 'Step 1 - Interview Not Required'),
        ('step_1b_interview_scheduled', 'Step 1 - Interview Scheduled'),
        ('step_1c_interview_completed', 'Step 1 - Interview Completed'),
        
        ('step_2_send_offer', 'Step 2 - Send Offer to Mentor'),
        ('step_2a_offer_sent', 'Step 2 - Offer Sent to Mentor'),
        ('step_2b_offer_accepted', 'Step 2 - Offer Accepted'),
        ('step_2c_offer_declined', 'Step 2 - Offer Declined'),
        
        ('step_3_send_contract', 'Step 3 - Send Contract to Mentor'),
        ('step_3a_contract_sent', 'Step 3 - Contract Sent to Mentor'),
        
        ('step_4_contract_signed_by_mentor', 'Step 4 - Contract Signed by Mentor Only'),
        ('step_4a_contract_signed_by_admin', 'Step 4 - Contract Signed by Admin Only'),
        ('step_4b_contract_completed', 'Step 4 - Contract Signing Complete'),
        
        ('step_5_send_calendar_invites', 'Step 5 - Send Calendar Invites'),
        ('step_5a_calendar_invites_sent', 'Step 5 - Calendar Invites Sent'),
        
        ('step_6_onboard_mentor', 'Step 6 - Onboard Mentor'),
        ('step_6a_mentor_onboarded', 'Step 6 - Mentor Onboarded'),
        
        ('step_7_mentoring', 'Step 7 - Mentoring in Program'),
        
        ('step_8_collate_feedback', 'Step 8 - Collate Feedback for Mentor'),
        ('step_8a_feedback_sent', 'Step 8 - Feedback Sent to Mentor'),
        
        ('step_9_offboard_mentor', 'Step 9 - Offboard Mentor'),
        ('step_9a_offboarding_in_progress', 'Step 9 - Offboarding in Progress'),
        ('step_9b_mentor_offboarded', 'Step 9 - Mentor Offboarded')
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
    city = models.CharField(max_length=255, choices=CITY_CHOICES)

    #skills
    html_css = models.BooleanField()
    javascript = models.BooleanField()
    react = models.BooleanField()
    python = models.BooleanField()
    django = models.BooleanField()
    drf = models.BooleanField()

    # mentor types
    junior_mentor = models.BooleanField()
    industry_mentor = models.BooleanField()
    lead_mentor = models.BooleanField()
    she_codes_alumni = models.BooleanField()
    payment_type = models.CharField(max_length=255, choices=PAYMENT_TYPE_CHOICES)

    #steps
    current_step = models.CharField(max_length=255, choices=STEP_CHOICES)
    
    notes = models.TextField()
    feedback = models.TextField()
    is_active = models.BooleanField()

    #multiple options
    sessions = models.ManyToManyField(
        Session, related_name='mentors', blank=True, default=None
        )
    
    # Return the name of the mentors
    def __str__(self):

        return f"{self.first_name} {self.last_name}"
    
    
    # mentors = MentorSerializer(many=True, source="mentors", required=False)
    # sessions = models.ManyToManyField(Session, related_name='mentors', blank=True)
    #one option
    # session = models.ForeignKey(Session, on_delete=models.CASCADE, default=None)