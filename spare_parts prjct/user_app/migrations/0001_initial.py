# Generated by Django 5.0.6 on 2024-05-31 09:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('spare_part_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('pin_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('landmark', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'address_table',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('otp_created_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('total', models.IntegerField()),
                ('payment_method', models.CharField(max_length=100)),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.address')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spare_part_app.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.user')),
            ],
            options={
                'db_table': 'order_table',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.user'),
        ),
    ]
