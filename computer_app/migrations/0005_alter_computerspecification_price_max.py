# Generated by Django 4.2.2 on 2023-06-28 10:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_app', '0004_alter_computer_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='computerspecification',
            name='price_max',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MaxValueValidator(40000.0)]),
        ),
    ]