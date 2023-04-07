from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers, validators
from rest_framework.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

# /users/
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name","last_name","email", "is_active", "is_superuser","is_staff", "password")

        extra_kwargs = {
            "email": {
                "validators": [validators.UniqueValidator(queryset=CustomUser.objects.all())],
                "allow_blank": False,
                "required": True,
            },
            "password": {"write_only": True},
            "is_active": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])  # protects password
        user.save()
        return user

# /users/<id:pk>/
class CustomUserDetailSerializer(CustomUserSerializer):
        class Meta:
            model = CustomUser
            fields = (
                "id",
                "username",
                "first_name",
                "last_name",
                "email",
                "is_active",
                "is_staff",
                "is_superuser"
            )
            read_only_fields = ["id"]

# uses/current/change-password/
class CustomUserPasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ('old_password', 'new_password', 'confirm_password')

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise ValidationError('Passwords do not match.')
        return data



# https://stackoverflow.com/a/50472986
# https://www.django-rest-framework.org/api-guide/serializers/#customizing-serialization-classes
# Permission References https://realpython.com/manage-users-in-django-admin/