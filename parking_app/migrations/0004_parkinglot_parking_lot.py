# Generated by Django 4.2.7 on 2023-11-19 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking_app', '0003_remove_parkinglot_parking_lot'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinglot',
            name='parking_lot',
            field=models.JSONField(default=list),
        ),
    ]
