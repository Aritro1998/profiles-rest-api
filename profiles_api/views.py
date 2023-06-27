from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserProfileSerializer
from . import models
from rest_framework import serializers, viewsets
# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    # Handle creating and updating profiles
    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()