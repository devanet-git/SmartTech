# Generated by Django 4.0.3 on 2022-03-24 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0002_remove_phone_model_phone_pattern_phone_phone_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_models',
            field=models.CharField(blank=True, default='', max_length=64, null=True),
        ),
    ]