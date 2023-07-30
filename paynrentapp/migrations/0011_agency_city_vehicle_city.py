# Generated by Django 4.1.6 on 2023-05-30 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0010_vehicle_agency_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
    ]
