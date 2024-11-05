# Generated by Django 5.1.2 on 2024-10-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_item_notification_alter_sale_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='custom_item_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='stock_quantity',
            field=models.IntegerField(default=0),
        ),
    ]