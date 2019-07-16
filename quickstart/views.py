from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserSerializers, GroupSerializers
from django.contrib.auth.models import User, Group

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializers