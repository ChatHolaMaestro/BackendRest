# Generated by Django 4.1.7 on 2023-03-28 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalrelative',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='historicalstudent',
            name='grade',
            field=models.CharField(choices=[('PJD', 'Pre-Jardín'), ('JD', 'Jardín'), ('TR', 'Transición'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=3, verbose_name='Grado'),
        ),
        migrations.AlterField(
            model_name='historicalstudent',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='relative',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('PJD', 'Pre-Jardín'), ('JD', 'Jardín'), ('TR', 'Transición'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11')], max_length=3, verbose_name='Grado'),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, verbose_name='Número de teléfono'),
        ),
    ]
