from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Session
from .serializers import SessionSerializer, SessionDetailSerializer
from mentors.permissions import IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# /sessions/
class SessionList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

# /sessions/<id:pk>/
class SessionDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = Session.objects.all()
    serializer_class = SessionDetailSerializer