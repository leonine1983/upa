# Generated by Django 4.2 on 2023-07-10 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0095_atendimento_especializado_pk_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='triagem',
            name='atend_especializado',
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='pk_paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Triagem.triagem'),
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('0', 'Aguardando'), ('2', 'Liberado'), ('1', 'Em atendimento')], max_length=30, null=True),
        ),
    ]
