from django.urls import path

from . import views

# to use the new user view add the urls

urlpatterns = [
    path("", views.CustomUserList.as_view(), name="customuser-list"),
    path("<int:pk>/", views.CustomUserDetailView.as_view(), name="customuser-detail"),
    path("session/", views.SessionUserDetailView.as_view(), name="session"),
]