# Generated by Django 5.0 on 2024-10-23 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(5)], verbose_name='Nome do Artista')),
                ('artistic_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)], verbose_name='Nome Artistico')),
                ('biography', models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(0)], verbose_name='Biografia do Artista')),
                ('follower', models.IntegerField(default=0)),
                ('nr_album', models.IntegerField(default=1)),
                ('gender', models.CharField(choices=[('POP', 'Pop'), ('ELETONICA', 'Eletronica'), ('PAGODE', 'Pagode'), ('ROCK', 'Rock'), ('RAP', 'Rap'), ('SAMBA', 'Samba')], max_length=10, verbose_name='Genero')),
                ('creation_date', models.DateField(auto_now=True, verbose_name='Data de Criação')),
                ('nr_plays', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
