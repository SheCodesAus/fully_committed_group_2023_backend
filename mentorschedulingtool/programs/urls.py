from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='program-list'),
    path('programs/<int:pk>/', views.ProgramListDetail.as_view(), name='program-list-detail'),
]