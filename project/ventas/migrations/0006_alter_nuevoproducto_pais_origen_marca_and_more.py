# Generated by Django 5.0.4 on 2024-05-09 12:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_pais_nuevoproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuevoproducto',
            name='pais_origen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.pais'),
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(error_messages={'unique': 'Esa marca ya esta registrada.'}, max_length=100, unique=True)),
                ('pais_origen', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.pais')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.AddField(
            model_name='nuevoproducto',
            name='marca',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.marca'),
        ),
    ]