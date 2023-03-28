from django.contrib import admin
from .models import Program

# # Register your models here.

# -----------------------
# ADMIN BLOCK
class ProgramAdmin(admin.ModelAdmin):
    list_display = '__all__'

admin.site.register(Program)