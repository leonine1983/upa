# Generated by Django 4.1.4 on 2023-03-05 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0040_rename_paciente_chamar_paciente'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Chamar_Paciente',
        ),
    ]
