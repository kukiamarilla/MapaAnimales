# Generated by Django 2.2.2 on 2020-04-26 23:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0008_auto_20200404_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datos_adopcion',
            fields=[
                ('identificativo', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.CharField(default=0, max_length=40)),
                ('fecha', models.DateField(default=datetime.datetime(2020, 4, 26, 23, 20, 22, 617707, tzinfo=utc))),
                ('descripcion', models.TextField(default='Sin descripcion', max_length=400)),
                ('animal', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=20)),
                ('edad_animal', models.IntegerField(default=1)),
                ('numero_telefono_persona', models.CharField(default='0975209464', max_length=40)),
                ('latitud_persona', models.FloatField()),
                ('longitud_persona', models.FloatField()),
                ('imagen', models.ImageField(default='imagenes/None/no-img.jpg', upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='datos',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 4, 26, 23, 20, 22, 615614, tzinfo=utc)),
        ),
    ]
