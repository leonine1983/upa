# Generated by Django 4.2.7 on 2023-12-04 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0036_alter_medico_atendimento_paciente_medico_atendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamar_p_para_atendimento',
            name='nome_paciente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Medicos.medico_atendimento'),
        ),
    ]
