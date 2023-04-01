from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mentor
from .serializers import MentorSerializer
from .permissions import IsSuperUserOrReadOnly
# Create your views here.

class MentorList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorListDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer