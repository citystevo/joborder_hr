# Generated by Django 4.2 on 2024-10-16 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_product_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_date',
            new_name='date_created',
        ),
    ]