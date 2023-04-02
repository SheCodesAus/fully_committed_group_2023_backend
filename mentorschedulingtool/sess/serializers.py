from rest_framework import serializers
from mentors.serializers import MentorWithoutSessionsSerializer

from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    mentors = MentorWithoutSessionsSerializer(many=True, read_only=True)
    total_mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = [
            'id', 
            'session_name', 
            'total_mentors_required', 
            'total_mentors_assigned', 
            'date', 'city', 
            'module_type', 
            'program', 
            'mentors',
            'junior_mentors_required',
            'industry_mentors_required',
            'lead_mentors_required'
        ]
        read_only_fields = ['id','total_mentors_required','total_mentors_assigned']

