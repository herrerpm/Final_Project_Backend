# Generated by Django 4.1.3 on 2022-11-19 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Correo', models.EmailField(max_length=254)),
                ('Contrasena', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Aerolinea', models.CharField(max_length=30)),
                ('Salida', models.CharField(max_length=30)),
                ('Llegada', models.CharField(max_length=30)),
                ('Tiempo_salida', models.DateTimeField()),
                ('Tiempo_llegada', models.DateTimeField()),
                ('Maletas', models.PositiveSmallIntegerField()),
                ('Asiento', models.CharField(max_length=5)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flightapi.user')),
            ],
        ),
    ]
