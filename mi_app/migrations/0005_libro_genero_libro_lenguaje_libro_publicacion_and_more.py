# Generated by Django 4.1 on 2024-12-08 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mi_app", "0004_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="libro",
            name="genero",
            field=models.CharField(default="Desconocido", max_length=30),
        ),
        migrations.AddField(
            model_name="libro",
            name="lenguaje",
            field=models.CharField(default="Desconocido", max_length=30),
        ),
        migrations.AddField(
            model_name="libro",
            name="publicacion",
            field=models.DateField(default="2000-01-01"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="libro",
            name="ventas",
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="libro",
            name="titulo",
            field=models.CharField(max_length=100),
        ),
    ]
