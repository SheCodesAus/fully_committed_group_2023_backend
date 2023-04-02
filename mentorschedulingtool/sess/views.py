from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Session
from .serializers import SessionSerializer
from mentors.permissions import IsSuperUserOrReadOnly
# Create your views here.

class SessionList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class SessionListDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer