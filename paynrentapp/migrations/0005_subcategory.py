# Generated by Django 4.1.6 on 2023-03-15 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paynrentapp', '0004_alter_category_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.CharField(default='', max_length=70)),
                ('company_name', models.CharField(default='', max_length=70)),
                ('subcategory_name', models.CharField(default='', max_length=70)),
                ('description', models.CharField(default='', max_length=150)),
                ('icon', models.ImageField(upload_to='static/')),
            ],
        ),
    ]
