# Generated by Django 4.2.7 on 2024-04-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0047_medico_atendimento_chamadas_contabilizadas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamar_p_para_atendimento',
            name='data_chamada',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]