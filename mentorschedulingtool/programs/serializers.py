from rest_framework import serializers
from .models import Program

from sess.serializers import SessionSerializer
from sess.models import Session

# trying to get the sessions to display with the program list. Not working.
# used same approach for session serializer and it worked. I don't know why it's not
class ProgramSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True, read_only=True)
    class Meta:
        model = Program
        fields = '__all__'