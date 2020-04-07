from rest_framework.serializers import ModelSerializer
from .models import CostCentreCode, Deliverable, HiringManager, Role, Team

class CostCentreCodeSerializer(ModelSerializer):
    class Meta:
        model = CostCentreCode
        fields = ('department', 'code')

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('name', 'description')

