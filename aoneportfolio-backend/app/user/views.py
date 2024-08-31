"""
Views for the user API.
"""
from rest_framework import generics, authentication, permissions, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from core.models import User
from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    """sign in the user and return the token."""
    def post(self, request, *args, **kwargs):
        """pass token to the user."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.name,
        })

    """sign out the user and delete the token."""
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class ManageUserView(viewsets.ModelViewSet):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset.filter(id=self.request.user.id)


class UserViewSet(viewsets.ModelViewSet):
    """Manage users in the database."""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        """Return objects for the current authenticated user only."""
        return self.queryset


