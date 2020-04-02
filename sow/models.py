from django.db import models

# Create your models here.

class StatementOfWork(models.Model):

    companyName = models.CharField(max_length=30)
    slotCode = models.CharField(max_length=30)
    nominatedWorker = models.BooleanField()  # checkbox
    

    LC = 'LC'
    DAVE = 'DAVE'
    NM = 'NM'
    DEFAULT_HM = 'DEFAULT'

    hmChoices = [
        (LC, 'Liz Catherall'),
        (DAVE, 'Dave Matthews'),
        (NM, 'Nitesh Malvi'),
        (DEFAULT_HM, 'Please select a hiring manager...')
    ]

    hiringManager = models.CharField(
        max_length=30,
        choices = hmChoices,
        default = DEFAULT_HM
    )

    team = models.CharField(max_length=30)
    projectDescription = models.TextField()
    

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

    progCode = models.CharField(max_length=30)
    projCode = models.CharField(max_length=30)
    startDate = models.DateField
    endDate = models.DateField
    ir35 = models.CharField
    projectFee = models.DecimalField
    retentionFee = models.DecimalField
    contractEndMonth = models.DateField
    contractEndMothInc = models.DateField

    DM = 'DM'
    PM = 'PM'
    UR = 'UR'
    DEV = 'DEV'
    TA = 'TA'
    DES = 'DES'
    UXD = 'UXD'
    DEFAULT_ROLE = 'd'

    roleChoices = [
        (DM, 'Delivery Manager'),
        (PM, 'Product Manager'),
        (UR, 'User Researcher'),
        (DEV, 'Developer'),
        (TA, 'Technical Architect'),
        (DES, 'Designer'),
        (UXD, 'UX Designer'),
        (DEFAULT_ROLE, 'Please select a role...')
    ]

    role = models.CharField(
        max_length=30,
        choices=roleChoices,
        default=DEFAULT_ROLE
    )