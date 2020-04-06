from django.shortcuts import render
from .models import Role
from .serializers import RoleSerializer
from rest_framework import generics

# Create your views here.

class RoleList(generics.ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RoleDetail(generics.RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer