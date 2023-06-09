from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer

# /programs/
class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    mentors_required = serializers.ReadOnlyField()
    mentors_assigned = serializers.ReadOnlyField()
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'mentors_required',
            'mentors_assigned',
            'sessions'

        ]
        read_only_fields = ['id', 'mentors_required', 'mentors_assigned']

# /programs/<id:pk>/
class ProgramDetailSerializer(ProgramSerializer):
    # sessions = SessionSerializer(many=True, read_only=True)
    # mentors_assigned = serializers.ReadOnlyField()
    # mentors_required = serializers.ReadOnlyField()
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'mentors_required',
            'mentors_assigned',
            'sessions'
        ]
        read_only_fields = ['id']