from django.contrib import admin
# from .models import Mentor
from .models import Mentor, MentorNote

# # Register your models here.

# -----------------------
# ADMIN BLOCK
class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name','last_name', 'email','city', 'is_active')
    model = Mentor


admin.site.register(Mentor, MentorAdmin)

class MentorNoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_on','noter', 'notes_type','mentor')
    model = MentorNote


admin.site.register(MentorNote, MentorNoteAdmin)
