# Generated by Django 4.1.6 on 2023-02-28 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0002_category_iconee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='iconee',
        ),
    ]
