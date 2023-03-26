from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        # (
        #     "Additional User Information",
        #     {
        #         "fields": (
        #             "bio",
        #             "avatar",
        #         )
        #     },
        # ),
    )

admin.site.register(CustomUser, CustomUserAdmin)