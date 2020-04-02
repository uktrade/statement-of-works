from django.db import models

# Create your models here.

class Role(models.Model):
    class Meta:
        ordering = ['roleName']
    
    def __str__(self):
        return self.roleName

    roleName = models.CharField(max_length = 30)
    roleDescription = models.TextField(blank=True)

class StatementOfWork(models.Model):

    companyName = models.CharField(max_length=30)
    slotCode = models.CharField(max_length=30)
    nominatedWorker = models.BooleanField()  # checkbox
    
    HM1 = '1'
    HM2 = '2'
    HM3 = '3'
    DEFAULT_HM = 'DEFAULT'

    hmChoices = [
        (HM1, 'option 1'),
        (HM2, 'option 2'),
        (HM3, 'option 3'),
        (DEFAULT_HM, 'Please select a hiring manager...')
    ]

    hiringManager = models.CharField(
        max_length=30,
        choices = hmChoices,
        default = DEFAULT_HM
    )

    DEFAULT_TEAM = 'DEFAULT'

    teamChoices = [
        (DEFAULT_TEAM, 'DDaT / Data Team')
    ]

    team = models.CharField(
        max_length=30,
        choices = teamChoices,
        default = DEFAULT_TEAM
        )

    projectDescription = models.TextField()

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    STRATEGY = 'ST'
    TECH = 'T'
    DIGITAL = 'DIG'
    DATA = 'DAT'
    DABOPS = 'DA'
    SPIRE = 'S'
    DEFAULT_CCODE = 'DEFAULT'

    ccChoices = [
        (STRATEGY, 'Strategy - 109711'),
        (TECH, 'Technology - 10971'),
        (DIGITAL, 'Digital - 109713'),
        (DATA, 'Data - 109714'),
        (DABOPS, 'DDaT Director and Business Operations - 109715'),
        (SPIRE, 'SPIRE - 109376'),
        (DEFAULT_CCODE, 'Please select a cost code...')

    ]

    costCentreCode = models.CharField(
        max_length=30,
        choices=ccChoices,
        default=DEFAULT_CCODE
    )

    progCode = models.CharField(max_length=30, blank=True)
    projCode = models.CharField(max_length=30, blank=True)
    startDate = models.DateField
    endDate = models.DateField
    ir35 = models.BooleanField(default=False)
    projectFee = models.DecimalField
    retentionFee = models.DecimalField
    contractEndMonth = models.DateField
    contractEndMothInc = models.DateField

    