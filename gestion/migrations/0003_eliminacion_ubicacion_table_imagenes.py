# Generated by Django 4.2.2 on 2023-06-23 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_agregue_columna_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name_plural': 'Imagenes'},
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='isStaff',
            new_name='is_staff',
        ),
        migrations.RemoveField(
            model_name='imagen',
            name='ubicacion',
        ),
    ]
