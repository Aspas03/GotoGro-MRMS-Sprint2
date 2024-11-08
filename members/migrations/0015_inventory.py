# Generated by Django 5.1.2 on 2024-11-02 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_alter_sale_item_name_delete_notification_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=255, unique=True)),
                ('inventory_amount', models.IntegerField(default=0)),
            ],
        ),
    ]
