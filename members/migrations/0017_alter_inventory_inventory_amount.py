# Generated by Django 5.1.2 on 2024-11-02 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0016_inventory_remaining_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='inventory_amount',
            field=models.IntegerField(default=1000),
        ),
    ]
