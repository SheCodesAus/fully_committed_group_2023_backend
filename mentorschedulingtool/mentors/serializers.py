from rest_framework import serializers
# from sess.serializers import SessionSerializer

from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    #TODO: ASSIGN A SESSION TO THIS MENTOR
    #TODO: DISPLAY THE LIST OF SESSIONS THIS MENTOR IS ASSIGNED TO
    #BUG: Circular reference issue. Revisit Crowdfunding backend for help
    
    # sessions = SessionSerializer(many=True, source="sessions", required=False)
    class Meta:
        model = Mentor
        fields = '__all__'

