# Generated by Django 5.0.2 on 2024-04-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
                ('stock', models.IntegerField()),
                ('genero', models.CharField(choices=[('1', 'Acción'), ('2', 'Aventura'), ('3', 'Carrera')], max_length=1, verbose_name='Genero')),
            ],
        ),
    ]