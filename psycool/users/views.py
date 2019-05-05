"""Users app views"""

from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .models import Patient, Psychologist
from .serializers import (
    UserSerializer, AuthTokenSerializer,
    PatientSerializer, PsychologistSerializer
)


class CreateUserView(generics.CreateAPIView):
    """Creates a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of an object to edit it."""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class PatientList(generics.ListCreateAPIView):
    """List all patients, and can GET them or POST one"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    """Gets the detail of a single patient and can GET, PUT or DELETE it"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    )
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PsychologistList(generics.ListCreateAPIView):
    """List all psychologists, and can GET them or POST one"""
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer


class PsychologistDetail(generics.RetrieveUpdateDestroyAPIView):
    """Gets the detail of a single psychologist and GET, PUT or DELETE it"""
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    )
    queryset = Psychologist.objects.all()
    serializer_class = PsychologistSerializer
