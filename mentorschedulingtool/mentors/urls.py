from django.urls import path
from . import views
urlpatterns = [
    path('mentors/', views.MentorList.as_view(), name='mentor-list'),
]