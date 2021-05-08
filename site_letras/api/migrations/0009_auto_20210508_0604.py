# Generated by Django 3.2 on 2021-05-08 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_artista_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='grupo',
        ),
        migrations.RemoveField(
            model_name='cancao',
            name='grupo',
        ),
        migrations.AlterField(
            model_name='artista',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.DeleteModel(
            name='Grupo',
        ),
    ]