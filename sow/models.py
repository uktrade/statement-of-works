from django.db import models
from datetime import date

# Create your models here.

class Role(models.Model):
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    name = models.CharField(max_length = 30)
    description = models.TextField(blank=True)

class Deliverable(models.Model):
    """Deliverable model."""
    class Meta:
        ordering = ['role', 'title']

    def __str__(self):
        return self.title 

    title = models.CharField(max_length=200)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class HiringManager(models.Model):
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    name = models.CharField(max_length=100)

class Team(models.Model):
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)

class CostCentreCode(models.Model):
    class Meta:
        ordering = ['department']

    def __str__(self):
        return self.department + ' - %d' % self.code

    department = models.CharField(max_length=50)
    code = models.IntegerField()

class StatementOfWork(models.Model):
    company_name = models.CharField(max_length=160)
    slot_code = models.CharField(max_length=5)
    nominated_worker = models.BooleanField()
    hiring_manager = models.ForeignKey(HiringManager, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    project_description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    cost_centre_code = models.ForeignKey(CostCentreCode, on_delete=models.CASCADE)
    prog_code = models.CharField(max_length=30, blank=True)
    proj_code = models.CharField(max_length=30, blank=True)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    ir35 = models.BooleanField(default=False)
    project_fee = models.DecimalField(decimal_places=2, max_digits=5)
    retention_fee = models.DecimalField(decimal_places=2, max_digits=5)
    contract_end_month = models.DateField(default=date.today)
    contract_end_month_inc = models.DateField(default=date.today)