# Generated by Django 4.1.7 on 2023-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
    ]
