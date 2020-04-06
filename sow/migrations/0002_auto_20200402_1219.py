# Generated by Django 3.0.1 on 2020-04-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sow', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='statementofwork',
            name='ir35',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='statementofwork',
            name='progCode',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='statementofwork',
            name='projCode',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]