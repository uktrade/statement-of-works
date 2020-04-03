# Generated by Django 3.0.1 on 2020-04-03 13:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sow', '0008_auto_20200403_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementofwork',
            name='contract_end_month',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='statementofwork',
            name='contract_end_month_inc',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='statementofwork',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='statementofwork',
            name='project_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementofwork',
            name='retention_fee',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statementofwork',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
