# Generated by Django 2.2.2 on 2019-07-29 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kiosco_app', '0002_egreso_ingreso_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=models.CharField(max_length=150),
        ),
    ]
