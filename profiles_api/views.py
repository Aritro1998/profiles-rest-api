from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from . import models
from rest_framework import filters, viewsets
from rest_framework.authentication import TokenAuthentication
from . import permissions
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    # Handle creating and updating profiles
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)