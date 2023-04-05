from django.urls import path
from . import views

urlpatterns = [
    path('mentors/', views.MentorList.as_view(), name='mentor-list'),
    path('mentors/<int:pk>/', views.MentorDetail.as_view(), name='mentor-detail'),
    path("mentor-notes/", views.MentorNoteList.as_view(), name="mentor-notes-list"),
    path("mentor-notes/<int:pk>/", views.MentorNoteDetail.as_view(), name="mentor-notes-detail"),
]