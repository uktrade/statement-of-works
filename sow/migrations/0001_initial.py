# Generated by Django 3.0.1 on 2020-04-06 14:27

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CostCentreCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
            ],
            options={
                'ordering': ['department'],
            },
        ),
        migrations.CreateModel(
            name='HiringManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StatementOfWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=160)),
                ('slot_code', models.CharField(max_length=5)),
                ('nominated_worker', models.BooleanField()),
                ('project_description', models.TextField()),
                ('prog_code', models.CharField(blank=True, max_length=30)),
                ('proj_code', models.CharField(blank=True, max_length=30)),
                ('start_date', models.DateField(default=datetime.date.today)),
                ('end_date', models.DateField(default=datetime.date.today)),
                ('ir35', models.BooleanField(default=False)),
                ('project_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('retention_fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('contract_end_month', models.DateField(default=datetime.date.today)),
                ('contract_end_month_inc', models.DateField(default=datetime.date.today)),
                ('cost_centre_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow.CostCentreCode')),
                ('hiring_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow.HiringManager')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow.Role')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Deliverable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sow.Role')),
            ],
            options={
                'ordering': ['role', 'title'],
            },
        ),
    ]