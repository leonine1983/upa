# Generated by Django 4.2.7 on 2023-11-29 15:32

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0034_alter_chamar_p_para_atendimento_nome_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico_atendimento',
            name='Diagnostico',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico_atendimento',
            name='conduta',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico_atendimento',
            name='exame_fisico',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='medico_atendimento',
            name='historico_doenca_atual_HDA',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
