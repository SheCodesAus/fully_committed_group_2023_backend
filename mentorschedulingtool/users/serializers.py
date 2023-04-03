from rest_framework import serializers
from .models import CustomUser
from rest_framework import serializers, validators

# /users/
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "username", "first_name","last_name","email", "is_active", "is_superuser", "password")

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
                "is_superuser"
            )
            read_only_fields = ["id"]

# https://stackoverflow.com/a/50472986
# https://www.django-rest-framework.org/api-guide/serializers/#customizing-serialization-classes
# Permission References https://realpython.com/manage-users-in-django-admin/