from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from . import models
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from . import permissions
from rest_framework.settings import api_settings
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    # Handle creating and updating profiles
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    # Handle creating user authentication tokens
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES