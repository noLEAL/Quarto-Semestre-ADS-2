# Generated by Django 5.0 on 2024-10-14 14:04

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0006_person_passport'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reporter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('cpf', models.CharField(max_length=11)),
            ],
        ),
        migrations.AlterField(
            model_name='passport',
            name='issue_date',
            field=models.DateField(verbose_name='Data de Criação'),
        ),
        migrations.AlterField(
            model_name='person',
            name='cpf',
            field=models.CharField(max_length=11, validators=[django.core.validators.MinValueValidator(0)], verbose_name='CPF'),
        ),
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('publicado', models.DateField()),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.reporter')),
            ],
        ),
    ]