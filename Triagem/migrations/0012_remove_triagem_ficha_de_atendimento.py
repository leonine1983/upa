# Generated by Django 4.1.4 on 2023-01-02 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0011_rename_paciente_triagem_paciente_triagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triagem',
            name='ficha_de_atendimento',
        ),
    ]
