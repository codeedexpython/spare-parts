# Generated by Django 4.2.7 on 2024-05-31 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='vehicle',
        ),
        migrations.AddField(
            model_name='product',
            name='vehicle',
            field=models.ManyToManyField(related_name='product_vehicle', to='vehicle.vehicle'),
        ),
    ]