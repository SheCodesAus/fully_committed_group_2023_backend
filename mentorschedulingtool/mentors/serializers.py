from rest_framework import serializers

from .models import Mentor, MentorNote
# from .models import Mentor
from sess.models import Session



# /sessions/
# /mentors/
# sessions dropped from view, but available on detail. 
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'will_travel', 'city', 'html_css', 'javascript', 'react', 'python', 'django', 'drf', 'junior_mentor', 'industry_mentor', 'lead_mentor', 'she_codes_alumni', 'payment_type', 'current_step', 'is_active']
        # fields = ['id','first_name', 'last_name', 'email', 'will_travel', 'city', 'html_css', 'javascript', 'react', 'python', 'django', 'drf', 'junior_mentor', 'industry_mentor', 'lead_mentor', 'she_codes_alumni', 'payment_type', 'current_step', 'is_active']
# ----------------------
# /mentors/<id:pk>/
# removes circular import issue for MentorDetailSerializer below
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'

# ----------------------
# /mentor-notes/
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

# ----------------------
# /mentors/<id:pk>/
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
            'is_active', 
            'sessions',
            'mentornotes',
        ]

        read_only_fields = ['id']

