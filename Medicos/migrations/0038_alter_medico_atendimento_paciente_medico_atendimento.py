# Generated by Django 4.2.7 on 2023-12-06 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0170_alter_atendimento_especializado_situacao'),
        ('Medicos', '0037_alter_chamar_p_para_atendimento_nome_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_atendimento',
            name='paciente_medico_atendimento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='Triagem.triagem'),
        ),
    ]