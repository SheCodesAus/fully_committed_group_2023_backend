from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer,CustomUserDetailSerializer
from mentors.permissions import IsSuperUserOrReadOnly, IsOwnProfile

# /users/
class CustomUserList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# /users/<id:pk>/
class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

# /users/current/
class CurrentUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly, IsOwnProfile]
    lookup_field = 'id'
    serializer_class = CustomUserDetailSerializer

    def get_object(self):
        return self.request.user

