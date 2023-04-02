from rest_framework import serializers
from mentors.serializers import MentorWithoutSessionsSerializer


from .models import Session
from mentors.models import Mentor


class SessionSerializer(serializers.ModelSerializer):
    mentors = MentorWithoutSessionsSerializer(many=True, read_only=True)
    mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ['id', 'session_name', 'total_mentors_required', 'total_mentors_assigned', 'date', 'city', 'module_type', 'program', 'mentors']
        read_only_fields = ['id']

