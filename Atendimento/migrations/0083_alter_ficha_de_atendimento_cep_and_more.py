# Generated by Django 4.2.7 on 2024-02-28 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0082_remove_envio_triagem_retornou_em_menos_de_48_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='CEP',
            field=models.CharField(default='', max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='CPF',
            field=models.CharField(default='', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='RG',
            field=models.CharField(default='', max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='data_nascimento',
            field=models.DateField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='nacionalidade',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='nome_mae',
            field=models.CharField(default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='tel',
            field=models.CharField(default='', max_length=16, null=True),
        ),
    ]