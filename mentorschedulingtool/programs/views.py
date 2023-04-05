from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Program
from .serializers import ProgramSerializer, ProgramDetailSerializer
from mentors.permissions import IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# /programs/
class ProgramList (generics.ListCreateAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer


# /programs/<id:pk>/
class ProgramListDetail (generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Program.objects.all()
    serializer_class = ProgramDetailSerializer