# Generated by Django 4.2.2 on 2023-06-22 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('ubicacion', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'imagenes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('fechaVencimiento', models.DateField(db_column='fecha_vencimiento')),
                ('lote', models.TextField()),
                ('precio', models.FloatField()),
                ('categoria', models.ForeignKey(db_column='categoria_id', on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='gestion.categoria')),
                ('imagen', models.OneToOneField(db_column='imagen_id', on_delete=django.db.models.deletion.RESTRICT, related_name='producto', to='gestion.imagen')),
            ],
            options={
                'db_table': 'productos',
                'ordering': ['nombre', '-fechaVencimiento'],
            },
        ),
        migrations.AddField(
            model_name='categoria',
            name='imagen',
            field=models.OneToOneField(db_column='imagen_id', on_delete=django.db.models.deletion.RESTRICT, to='gestion.imagen'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('email', models.TextField(unique=True)),
                ('password', models.TextField()),
                ('tipo', models.TextField(choices=[('ADMIN', 'ADMIN'), ('CAJERO', 'CAJERO')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
    ]
