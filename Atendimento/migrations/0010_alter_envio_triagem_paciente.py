# Generated by Django 4.1.4 on 2022-12-31 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0009_alter_envio_triagem_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envio_triagem',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Atendimento.ficha_de_atendimento'),
        ),
    ]
