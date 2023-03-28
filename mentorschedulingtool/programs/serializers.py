from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer
from sess.models import Session



# i can simplify JSON file to just id of sessions if required. Let me know
class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    class Meta:
        model = Program
        fields = [
            'id',
            'program_name',
            'start_date',
            'end_date',
            'city',
            'program_type',
            'sessions'
        ]
        read_only_fields = ['id']