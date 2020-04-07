from django.shortcuts import render
from .models import CostCentreCode, Deliverable, HiringManager, Role, Team
from .serializers import CostCentreCodeSerializer, DeliverableSerializer, HiringManagerSerializer, RoleSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.

class CostCentreCodeList(ListAPIView):
    """List API view for CostCentreCode."""
    queryset = CostCentreCode.objects
    serializer_class = CostCentreCodeSerializer

class CostCentreCodeDetail(RetrieveAPIView):
    """List API view for one CostCentreCode."""
    queryset = CostCentreCode.objects
    serializer_class = CostCentreCodeSerializer

class DeliverableList(ListAPIView):
    """List API view for Deliverable."""
    queryset = Deliverable.objects
    serializer_class = DeliverableSerializer

class DeliverableDetail(RetrieveAPIView):
    """List API view for one Deliverable."""
    queryset = Deliverable.objects
    serializer_class = DeliverableSerializer

class HiringManagerList(ListAPIView):
    """List API view for HiringManager."""
    queryset = HiringManager.objects
    serializer_class = HiringManagerSerializer

class HiringManagerDetail(RetrieveAPIView):
    """List API view for one HiringManager."""
    queryset = HiringManager.objects
    serializer_class = HiringManagerSerializer

class RoleList(ListAPIView):
    """List API view for Roles."""
    queryset = Role.objects
    serializer_class = RoleSerializer

class RoleDetail(RetrieveAPIView):
    """List API view for a single Role."""
    queryset = Role.objects
    serializer_class = RoleSerializer