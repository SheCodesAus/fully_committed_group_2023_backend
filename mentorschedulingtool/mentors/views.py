from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mentor
from .serializers import MentorSerializer
# Create your views here.

class MentorList (generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

class MentorListDetail (generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer