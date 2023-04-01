from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program
from .serializers import ProgramSerializer
from mentors.permissions import IsSuperUserOrReadOnly
# Create your views here.

class ProgramList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class ProgramListDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer