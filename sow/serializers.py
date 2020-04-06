from rest_framework.serializers import ModelSerializer
from .models import CostCentreCode, Deliverable, HiringManager, Role, Team

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('name', 'description')