from django.urls import path

from . import views

# to use the new user view add the urls

urlpatterns = [
    path("users/", views.CustomUserList.as_view(), name="customuser-list"),
    path("users/<int:pk>/", views.CustomUserDetailView.as_view(), name="customuser-detail"),
    path("users/current/", views.CurrentUserDetailView.as_view(), name="current"),
    path("users/current/change-password/", views.ChangePasswordView.as_view(), name="change-password"),
]