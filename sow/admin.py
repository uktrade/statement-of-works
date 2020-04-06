from django.contrib import admin
from .models import CostCentreCode, Deliverable, HiringManager, Role, StatementOfWork, Team

# Register your models here.
admin.site.register(StatementOfWork)
admin.site.register(Role)
admin.site.register(HiringManager)
admin.site.register(Team)
admin.site.register(Deliverable)
admin.site.register(CostCentreCode)