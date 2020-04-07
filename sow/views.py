from django.shortcuts import render
from .models import Role
from .serializers import RoleSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class RoleList(ListAPIView):
    """List API view for Roles."""
    queryset = Role.objects
    serializer_class = RoleSerializer

class RoleDetail(RetrieveAPIView):
    """List API view for a single Role."""
    queryset = Role.objects
    serializer_class = RoleSerializer