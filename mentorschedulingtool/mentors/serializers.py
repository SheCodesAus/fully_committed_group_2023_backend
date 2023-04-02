from rest_framework import serializers

from .models import Mentor, MentorNote
# from .models import Mentor
from sess.models import Session


# created for the session view - to avoid session repetition
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id','first_name', 'last_name', 'email', 'will_travel', 'city', 'html_css', 'javascript', 'react', 'python', 'django', 'drf', 'junior_mentor', 'industry_mentor', 'lead_mentor', 'she_codes_alumni', 'payment_type', 'current_step', 'notes', 'feedback', 'is_active']
# created to get full session view with session details on mentor list
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

class MentorNoteSerializer(serializers.ModelSerializer):
    noter = serializers.ReadOnlyField(source="noter.username")
    # mentor = MentorSerializer(many=True)
    class Meta:
        model = MentorNote
        fields = ["id", "created_on", "body", "noter", "notes_type", "mentor"]
        read_only_fields = [
            "id",
            "noter",
            "created_on"
        ]
        # fields = ["id", "created_on", "body", "notes_type", "mentor"]
        # read_only_fields = [
        #     "id"]

class MentorDetailSerializer(MentorSerializer):
    sessions = SessionSerializer(many=True)
    mentornotes = MentorNoteSerializer(many=True, read_only=True)

    class Meta:
        model = Mentor
        fields = [
            'id',
            'first_name', 
            'last_name', 
            'email', 
            'will_travel', 
            'city', 
            'html_css', 
            'javascript', 
            'react', 
            'python', 
            'django', 
            'drf', 
            'junior_mentor', 
            'industry_mentor', 
            'lead_mentor', 
            'she_codes_alumni', 
            'payment_type', 
            'current_step', 
            'notes', 
            'feedback', 
            'is_active', 
            'sessions',
            'mentornotes',
        ]

        read_only_fields = ['id']

