from rest_framework.serializers import ModelSerializer
from .models import CostCentreCode, Deliverable, HiringManager, Role, Team

class CostCentreCodeSerializer(ModelSerializer):
    class Meta:
        model = CostCentreCode
        fields = ('department', 'code')

class DeliverableSerializer(ModelSerializer):
    class Meta:
        model = Deliverable
        fields = ('title', 'description', 'role')

class HiringManagerSerializer(ModelSerializer):
    class Meta:
        model = HiringManager
        fields = ('name',)

class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('name', 'description')

class TeamSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ('name',)

