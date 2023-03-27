from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.MentorList.as_view(), name='mentor-list'),
    path('mentors/<int:pk>/', views.MentorListDetail.as_view(), name='mentor-list-detail'),
]