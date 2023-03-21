# Generated by Django 4.1.7 on 2023-03-21 13:18

import apps.users.models.user
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, help_text='Nombre de pila', max_length=100, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(blank=True, help_text='Apellidos completos', max_length=100, verbose_name='Apellidos')),
                ('identification_type', models.CharField(blank=True, choices=[('TI', 'Tarjeta de Identidad'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('NUIP', 'Número Único de Identificación Personal'), ('PA', 'Pasaporte')], max_length=5, verbose_name='Tipo de identificación')),
                ('identification_number', models.CharField(blank=True, help_text='Número de identificación sin puntos ni guiones', max_length=20, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_identification_number', message='El número de identificación debe ser solo números sin puntos, guiones o espacios.', regex='^\\d+$')], verbose_name='Número de identificación')),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='El número de teléfono debe ser solo números sin puntos, guiones o espacios.', regex='^\\d+$')], verbose_name='Número de teléfono')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha de eliminación')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Correo electrónico')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Superusuario')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Administrador'), (2, 'Profesor'), (3, 'Director de escuela')], default=2, verbose_name='Rol')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', apps.users.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, help_text='Nombre de pila', max_length=100, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(blank=True, help_text='Apellidos completos', max_length=100, verbose_name='Apellidos')),
                ('identification_type', models.CharField(blank=True, choices=[('TI', 'Tarjeta de Identidad'), ('CC', 'Cédula de Ciudadanía'), ('CE', 'Cédula de Extranjería'), ('NUIP', 'Número Único de Identificación Personal'), ('PA', 'Pasaporte')], max_length=5, verbose_name='Tipo de identificación')),
                ('identification_number', models.CharField(blank=True, db_index=True, help_text='Número de identificación sin puntos ni guiones', max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_identification_number', message='El número de identificación debe ser solo números sin puntos, guiones o espacios.', regex='^\\d+$')], verbose_name='Número de identificación')),
                ('phone_number', models.CharField(blank=True, max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='El número de teléfono debe ser solo números sin puntos, guiones o espacios.', regex='^\\d+$')], verbose_name='Número de teléfono')),
                ('id', models.BigIntegerField(blank=True, db_index=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de creación')),
                ('modified_date', models.DateTimeField(blank=True, editable=False, verbose_name='Fecha de modificación')),
                ('deleted_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Fecha de eliminación')),
                ('email', models.EmailField(db_index=True, max_length=255, verbose_name='Correo electrónico')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='Superusuario')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='Staff')),
                ('role', models.PositiveSmallIntegerField(choices=[(1, 'Administrador'), (2, 'Profesor'), (3, 'Director de escuela')], default=2, verbose_name='Rol')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Usuario',
                'verbose_name_plural': 'historical Usuarios',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
