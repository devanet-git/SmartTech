# Generated by Django 4.0.3 on 2022-03-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0018_sensor_fingerprint_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storage',
            name='size',
        ),
        migrations.AddField(
            model_name='storage',
            name='size',
            field=models.FloatField(default=64),
        ),
    ]
