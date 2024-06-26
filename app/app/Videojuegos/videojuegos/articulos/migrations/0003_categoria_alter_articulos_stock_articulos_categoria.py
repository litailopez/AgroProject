# Generated by Django 5.0.2 on 2024-04-08 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_alter_articulos_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripcion')),
            ],
        ),
        migrations.AlterField(
            model_name='articulos',
            name='stock',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='articulos',
            name='categoria',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='articulos.categoria', verbose_name='Categoria'),
            preserve_default=False,
        ),
    ]
