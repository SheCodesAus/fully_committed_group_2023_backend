from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer
from sess.models import Session



# i can simplify JSON file to just id of sessions if required. Let me know
class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    mentors_required = serializers.ReadOnlyField()
    mentors_assigned = serializers.ReadOnlyField()
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'mentors_required',
            'mentors_assigned',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'sessions'

        ]
        read_only_fields = ['id', 'mentors_required', 'mentors_assigned']