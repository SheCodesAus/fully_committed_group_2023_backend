from django.contrib import admin
from .models import Mentor

# # Register your models here.

# -----------------------
# ADMIN BLOCK
class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'email','city', 'is_active', 'date_created')

admin.site.register(Mentor)