# Generated by Django 4.2.7 on 2024-01-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0079_alter_envio_triagem_retornou_em_menos_de_48_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio_triagem',
            name='horas48',
            field=models.BooleanField(default=False),
        ),
    ]
