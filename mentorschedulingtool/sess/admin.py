from django.contrib import admin

from .models import Session

# # Register your models here.

# -----------------------
# ADMIN BLOCK
class SessionAdmin(admin.ModelAdmin):
    list_display = ('id','session_name')

admin.site.register(Session)