from rest_framework import serializers


from .models import Mentor

# created for the session view - to avoid session repetition
class MentorWithoutSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        exclude = ('sessions', )
class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mentor
        fields = '__all__'

