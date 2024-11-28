# Generated by Django 5.1.2 on 2024-11-28 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Putovanje',
            fields=[
                ('putovanje_sifraPutovanja', models.IntegerField(primary_key=True, serialize=False)),
                ('putovanje_naslov', models.CharField(max_length=100)),
                ('putovanje_opis', models.TextField()),
                ('putovanje_lokacija', models.CharField(max_length=100)),
                ('putovanje_drzava', models.CharField(max_length=100)),
                ('putovanje_cijena', models.DecimalField(decimal_places=2, max_digits=10)),
                ('putovanje_datumPolaska', models.DateField()),
                ('putovanje_brojNocenja', models.IntegerField()),
                ('putovanje_brojOsoba', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Prijave',
            fields=[
                ('prijava_sifraPrijave', models.IntegerField(primary_key=True, serialize=False)),
                ('prijava_vrstaAranzmana', models.CharField(max_length=100)),
                ('prijava_brojOsoba', models.IntegerField()),
                ('putovanje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.putovanje')),
            ],
        ),
    ]
