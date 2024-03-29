# Generated by Django 4.1.4 on 2023-02-09 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0033_triagem_atestado_triagem_encaminhamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='atestado',
            field=models.TextField(default='Digite o atestado o paciente aqui', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='encaminhamento',
            field=models.TextField(default='Digite o encaminhamento do paciente', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='exames',
            field=models.TextField(default='Preencha com a relação de exames', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='preescrever_medicamento_medico',
            field=models.TextField(default='Preescreva o medicamento para o paciente', max_length=500, null=True),
        ),
    ]
