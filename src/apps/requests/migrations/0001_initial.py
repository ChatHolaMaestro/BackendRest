# Generated by Django 4.1.7 on 2023-03-21 13:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0001_initial'),
        ('subjects', '0001_initial'),
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('status', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADO', 'Completado'), ('CONTACTADO', 'Contactado'), ('CANCELADO', 'Cancelado')], default='CONTACTADO', max_length=20)),
                ('request_type', models.CharField(choices=[('TAREAS', 'Apoyo en Tareas'), ('REFUERZO', 'Refuerzo Académico')], default='TAREAS', max_length=20)),
                ('contact_times', models.IntegerField(default=0)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subjects.subject')),
                ('teacher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
        migrations.CreateModel(
            name='HistoricalRequest',
            fields=[
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('status', models.CharField(choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADO', 'Completado'), ('CONTACTADO', 'Contactado'), ('CANCELADO', 'Cancelado')], default='CONTACTADO', max_length=20)),
                ('request_type', models.CharField(choices=[('TAREAS', 'Apoyo en Tareas'), ('REFUERZO', 'Refuerzo Académico')], default='TAREAS', max_length=20)),
                ('contact_times', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='students.student')),
                ('subject', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='subjects.subject')),
                ('teacher', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='teachers.teacher')),
            ],
            options={
                'verbose_name': 'historical Solicitud',
                'verbose_name_plural': 'historical Solicitudes',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
