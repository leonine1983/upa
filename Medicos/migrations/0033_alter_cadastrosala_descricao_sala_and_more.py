# Generated by Django 4.2.7 on 2023-11-23 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0032_alter_medico_atendimento_paciente_medico_atendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastrosala',
            name='descricao_Sala',
            field=models.TextField(default='Ex.: Sala de atendimento pediátrico', max_length=200),
        ),
        migrations.AlterField(
            model_name='cadastrosala',
            name='nome_Sala',
            field=models.CharField(default='Ex: Sala de pediatria', max_length=40),
        ),
    ]