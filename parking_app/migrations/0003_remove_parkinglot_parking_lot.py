# Generated by Django 4.2.7 on 2023-11-19 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0002_parkinglot_parking_lot'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parkinglot',
            name='parking_lot',
        ),
    ]