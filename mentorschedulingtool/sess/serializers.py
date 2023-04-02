from rest_framework import serializers
from mentors.serializers import MentorWithoutSessionsSerializer

from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    mentors = MentorWithoutSessionsSerializer(many=True, read_only=True)
    total_mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = [

            # session details
            'id', 
            'session_name', 
            'date', 'city', 
            'module_type', 
            'program', 

            # mentor counts
            'junior_mentors_required',
            'industry_mentors_required',
            'lead_mentors_required',
            'total_mentors_required', 
            'total_mentors_assigned',

            # mentors
            'mentors'
        ]
        read_only_fields = ['id','total_mentors_required','total_mentors_assigned']