from django.contrib import admin
from .models import StatementOfWork, Role

#class RoleAdmin(admin.ModelAdmin):
#    list_display = ('roleName')

# Register your models here.
admin.site.register(StatementOfWork)
admin.site.register(Role)#, RoleAdmin)