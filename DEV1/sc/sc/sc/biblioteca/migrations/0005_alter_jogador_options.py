# Generated by Django 5.0 on 2024-10-14 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_jogador_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jogador',
            options={'verbose_name_plural': 'Jogadores'},
        ),
    ]
