from django.db import models

# Create your models here.

class Role(models.Model):
    class Meta:
        ordering = ['role_name']
    
    def __str__(self):
        return self.role_name

    role_name = models.CharField(max_length = 30)
    role_description = models.TextField(blank=True)
    role_deliverable1 = models.TextField(blank=True)
    role_deliverable2 = models.TextField(blank=True)

class StatementOfWork(models.Model):

    company_name = models.CharField(max_length=30)
    slot_code = models.CharField(max_length=5)
    nominated_worker = models.BooleanField()  # checkbox
    
    HM1 = '1'
    HM2 = '2'
    HM3 = '3'
    DEFAULT_HM = 'DEFAULT'

    hm_choices = [
        (HM1, 'option 1'),
        (HM2, 'option 2'),
        (HM3, 'option 3'),
        (DEFAULT_HM, 'Please select a hiring manager...')
    ]

    hiring_manager = models.CharField(
        max_length=30,
        choices = hm_choices,
        default = DEFAULT_HM
    )

    DEFAULT_TEAM = 'DEFAULT'

    team_choices = [
        (DEFAULT_TEAM, 'DDaT / Data Team')
    ]

    team = models.CharField(
        max_length=30,
        choices = team_choices,
        default = DEFAULT_TEAM
        )

    project_description = models.TextField()

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    STRATEGY = 'ST'
    TECH = 'T'
    DIGITAL = 'DIG'
    DATA = 'DAT'
    DABOPS = 'DA'
    SPIRE = 'S'
    DEFAULT_CCODE = 'DEFAULT'

    cc_choices = [
        (STRATEGY, 'Strategy - 109711'),
        (TECH, 'Technology - 10971'),
        (DIGITAL, 'Digital - 109713'),
        (DATA, 'Data - 109714'),
        (DABOPS, 'DDaT Director and Business Operations - 109715'),
        (SPIRE, 'SPIRE - 109376'),
        (DEFAULT_CCODE, 'Please select a cost code...')

    ]

    cost_centre_code = models.CharField(
        max_length=30,
        choices=cc_choices,
        default=DEFAULT_CCODE
    )

    prog_code = models.CharField(max_length=30, blank=True)
    proj_code = models.CharField(max_length=30, blank=True)
    start_date = models.DateField
    end_date = models.DateField
    ir35 = models.BooleanField(default=False)
    project_fee = models.DecimalField
    retention_fee = models.DecimalField
    contract_end_month = models.DateField
    contract_end_month_inc = models.DateField

    