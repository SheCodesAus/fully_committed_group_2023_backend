from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer
from sess.models import Session

class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    total_mentors_required = serializers.ReadOnlyField()
    total_mentors_assigned = serializers.ReadOnlyField()
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'total_mentors_required',
            'total_mentors_assigned',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'sessions'

        ]
        read_only_fields = ['id', 'total_mentors_required', 'total_mentors_assigned']