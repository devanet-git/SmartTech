# Generated by Django 4.0.3 on 2022-03-17 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0009_alter_camera_camera_model_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='num_of_camera',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
