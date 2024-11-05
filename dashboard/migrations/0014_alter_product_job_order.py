# Generated by Django 4.2 on 2024-10-23 13:38

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_product_production_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='job_order',
            field=models.CharField(default=dashboard.models.generate_job_order, max_length=50, unique=True),
        ),
    ]