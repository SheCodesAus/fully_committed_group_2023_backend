from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mentor, MentorNote
from .serializers import MentorDetailSerializer, MentorNoteSerializer, MentorSerializer
from .permissions import IsSuperUserOrReadOnly
# Create your views here.

# /mentors/
class MentorList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

# /mentors/<id:pk>/
class MentorDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]
    queryset = Mentor.objects.all()
    serializer_class = MentorDetailSerializer

# /mentor-notes/
class MentorNoteList(generics.ListCreateAPIView):
    queryset = MentorNote.objects.all()
    serializer_class = MentorNoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(noter=self.request.user)

# /mentor-notes/<id:pk>/
class MentorNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentorNote.objects.all()
    serializer_class = MentorNoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly]