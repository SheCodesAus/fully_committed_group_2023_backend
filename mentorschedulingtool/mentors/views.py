from rest_framework import status, generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mentor, MentorNote
from .serializers import MentorDetailSerializer, MentorNoteSerializer, MentorSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework.permissions import IsAuthenticated

# -- API-Root Config
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

# /mentors/
class MentorList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

# /mentors/<id:pk>/
class MentorDetail (generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = Mentor.objects.all()
    serializer_class = MentorDetailSerializer

# /mentor-notes/
class MentorNoteList(generics.ListCreateAPIView):
    queryset = MentorNote.objects.all()
    serializer_class = MentorNoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(noter=self.request.user)

# /mentor-notes/<id:pk>/
class MentorNoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MentorNote.objects.all()
    serializer_class = MentorNoteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]

@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "mentors": reverse("mentor-list", request=request, format=format),
            "mentor-notes": reverse("mentor-notes-list", request=request, format=format),
            "sessions": reverse("session-list", request=request, format=format),
            "programs": reverse("program-list", request=request, format=format),
            "users": reverse("customuser-list", request=request, format=format),
        }
    )