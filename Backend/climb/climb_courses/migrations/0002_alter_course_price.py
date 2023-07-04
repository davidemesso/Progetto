# Generated by Django 4.2.2 on 2023-07-04 19:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('climb_courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.FloatField(verbose_name=django.core.validators.MinValueValidator(0)),
        ),
    ]