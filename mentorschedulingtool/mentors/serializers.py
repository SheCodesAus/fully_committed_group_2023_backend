from rest_framework import serializers

from .models import Mentor,Session

# created for the session view - to avoid session repetition
class MentorWithoutSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        exclude = ('sessions', )

# created to get full session view with session details
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
class MentorSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)

    class Meta:
        model = Mentor
        fields = '__all__'

