# Generated by Django 5.1.2 on 2024-11-02 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0013_rename_stock_quantity_item_remaining_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='item_name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='custom_item_name',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]