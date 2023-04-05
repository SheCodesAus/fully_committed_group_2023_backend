from rest_framework import serializers
from mentors.serializers import MentorSerializer, MentorDetailSerializer


from .models import Session
from mentors.models import Mentor

# /sessions/
class SessionSerializer(serializers.ModelSerializer):
    mentors = MentorSerializer(many=True, read_only=True)
    mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ['id', 'session_name', 'mentors_required', 'mentors_assigned', 'start_date','end_date','city', 'module_type', 'program', 'mentors']
        read_only_fields = ['id']

# /sessions/<id:pk>/
class SessionDetailSerializer(SessionSerializer):
    mentors = MentorDetailSerializer(many=True, read_only=True)
    mentors_assigned = serializers.ReadOnlyField()

    class Meta:
        model = Session
        fields = ['id', 'session_name', 'mentors_required', 'mentors_assigned', 'start_date','end_date','city', 'module_type', 'program', 'mentors']
        read_only_fields = ['id']