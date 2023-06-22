# Generated by Django 4.2.2 on 2023-06-22 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerBrands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='logos/')),
            ],
        ),
        migrations.CreateModel(
            name='ComputerSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generation', models.CharField(max_length=100)),
                ('price_min', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_max', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ram', models.IntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer_app.computerbrands')),
            ],
        ),
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('computer_code', models.CharField(max_length=100, unique=True)),
                ('quantity', models.IntegerField()),
                ('unit_rate', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('computer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='computer_app.computerspecification')),
            ],
        ),
    ]
