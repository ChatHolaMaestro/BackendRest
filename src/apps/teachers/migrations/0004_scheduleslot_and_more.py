# Generated by Django 4.1.7 on 2023-05-09 07:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teachers', '0003_remove_historicalschedule_day_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleSlot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('day_of_week', models.CharField(choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miércoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes'), ('SABADO', 'Sábado'), ('DOMINGO', 'Domingo')], default='LUNES', max_length=10, verbose_name='Día de la semana')),
                ('start_time', models.TimeField(verbose_name='Tiempo de inicio')),
                ('end_time', models.TimeField(verbose_name='Tiempo de finalización')),
                ('request_type', models.CharField(choices=[('TAREAS', 'Apoyo en Tareas'), ('REFUERZO', 'Refuerzo Académico'), ('CUALQUIERA', 'Cualquiera')], default='TAREAS', max_length=10, verbose_name='Tipo de solicitud')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_slots', to='teachers.teacher', verbose_name='Profesor')),
            ],
            options={
                'verbose_name': 'Horario',
                'verbose_name_plural': 'Horarios',
            },
        ),
        migrations.RenameModel(
            old_name='HistoricalSchedule',
            new_name='HistoricalScheduleSlot',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]
