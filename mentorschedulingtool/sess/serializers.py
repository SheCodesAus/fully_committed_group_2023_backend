from rest_framework import serializers
from mentors.serializers import MentorWithoutSessionsSerializer


from .models import Session
from mentors.models import Mentor

class SessionSerializer(serializers.ModelSerializer):
    mentors = MentorWithoutSessionsSerializer(many=True, read_only=True)
    mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = '__all__'

