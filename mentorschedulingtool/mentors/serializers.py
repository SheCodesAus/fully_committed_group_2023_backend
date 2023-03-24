from rest_framework import serializers
# for every model, create a serializer.
# You can use a model serializer - like a model form.
# Can build itself off a model. Automates

from .models import Mentor

class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'