from rest_framework import serializers
from mentors.serializers import MentorSerializer


from .models import Session
from mentors.models import Mentor

class SessionSerializer(serializers.ModelSerializer):
    #TODO: DISPLAY THE LIST OF MENTORS THAT HAVE BEEN ASSIGNED TO THIS SESSION
    #BUG: Circular reference issue. Revisit Crowdfunding backend for help
    
    # mentors = MentorSerializer(many=True, source="mentors", required=False)

    class Meta:
        model = Session
        fields = '__all__'