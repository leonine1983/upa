# Generated by Django 4.2.7 on 2023-12-27 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0222_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triagem',
            name='preescrever_medicamento_medico',
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Liberado', 'Liberado'), ('Em atendimento', 'Em atendimento'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
    ]
