# Generated by Django 4.2.7 on 2024-01-08 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0232_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Em atendimento', 'Em atendimento'), ('Liberado', 'Liberado'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
    ]
