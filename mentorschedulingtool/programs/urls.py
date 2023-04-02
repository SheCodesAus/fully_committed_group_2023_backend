from django.urls import path
from . import views

urlpatterns = [
    path('programs/', views.ProgramList.as_view(), name='program-list'),
    path('programs/<int:pk>/', views.ProgramDetail.as_view(), name='program-detail'),
]