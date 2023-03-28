from django.urls import path
from . import views

urlpatterns = [
    path('sessions/', views.SessionList.as_view(), name='session-list'),
    path('sessions/<int:pk>/', views.SessionListDetail.as_view(), name='session-list-detail'),
]