from rest_framework import serializers

from .models import Mentor

from sess.models import Session

# created for the session view - to avoid session repetition
class MentorWithoutSessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        # exclude = ('sessions', )

# created to get full session view with session details on mentor list
class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = '__all__'
class MentorSerializer(serializers.ModelSerializer):
    sessions = SessionSerializer(many=True)

    class Meta:
        model = Mentor
        fields = ['id','first_name', 'last_name', 'email', 'will_travel', 'city', 'html_css', 'javascript', 'react', 'python', 'django', 'drf', 'junior_mentor', 'industry_mentor', 'lead_mentor', 'she_codes_alumni', 'payment_type', 'current_step', 'notes', 'feedback', 'is_active', 'sessions']
        read_only_fields = ['id']

