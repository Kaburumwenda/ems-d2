# Generated by Django 3.2.5 on 2021-07-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_remove_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_cases', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('loc1', models.CharField(max_length=255)),
                ('loc12', models.CharField(max_length=255)),
                ('loc3', models.CharField(max_length=255)),
                ('fips', models.CharField(max_length=255)),
                ('gadm', models.CharField(max_length=255)),
                ('measurement_type', models.CharField(max_length=255)),
            ],
        ),
    ]
