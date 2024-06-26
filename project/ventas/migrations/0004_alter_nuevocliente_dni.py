# Generated by Django 5.0.4 on 2024-05-08 20:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_alter_localidad_localidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevocliente',
            name='DNI',
            field=models.CharField(error_messages={'unique': 'El DNI debe ir sin puntos'}, max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^\\d{7,8}$', 'Ingrese un máximo de 8 dígitos.')]),
        ),
    ]
