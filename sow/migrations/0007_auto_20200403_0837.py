# Generated by Django 3.0.1 on 2020-04-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sow', '0006_auto_20200403_0821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='roleDeliverables',
            new_name='roleDeliverable1',
        ),
        migrations.AddField(
            model_name='role',
            name='roleDeliverable2',
            field=models.TextField(blank=True),
        ),
    ]