# Generated by Django 4.2.7 on 2024-02-29 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0084_envio_triagem_retornou_em_menos_de_48_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='rua',
            field=models.CharField(default='', max_length=40, null=True),
        ),
    ]
