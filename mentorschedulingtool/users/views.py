from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import CustomUserSerializer,CustomUserDetailSerializer, CustomUserPasswordSerializer
from mentors.permissions import IsSuperUserOrReadOnly, IsOwnProfile

# /users/
class CustomUserList (generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

# /users/<id:pk>/
class CustomUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsSuperUserOrReadOnly, IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserDetailSerializer

# /users/current/
class CurrentUserDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsSuperUserOrReadOnly, IsOwnProfile]
    lookup_field = 'id'
    serializer_class = CustomUserDetailSerializer

    def get_object(self):
        return self.request.user

#/users/current/change-password/
class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = CustomUserPasswordSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': ['Wrong password.']},
                                status=status.HTTP_400_BAD_REQUEST)
            self.object.set_password(serializer.validated_data['new_password'])
            self.object.save()
            return Response({'status': 'password changed'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
