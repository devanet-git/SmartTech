# Generated by Django 4.0.3 on 2022-03-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0005_gps_gnss'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usb',
            name='version',
            field=models.CharField(max_length=128),
        ),
    ]
