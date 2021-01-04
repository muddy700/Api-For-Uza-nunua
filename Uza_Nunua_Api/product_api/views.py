from .serializers import LocationSerializer, ProfileSerializer, CategoriesSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import Location, Categories, Profile
from rest_framework import permissions
from django.shortcuts import render
from rest_framework import viewsets


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all().order_by('id')
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
