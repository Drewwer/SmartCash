# Generated by Django 3.1.2 on 2020-11-11 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_transferencia_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transferencia',
            old_name='imagen',
            new_name='imagenCarnet',
        ),
    ]
