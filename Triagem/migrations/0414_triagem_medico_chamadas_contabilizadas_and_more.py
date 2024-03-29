# Generated by Django 4.2.7 on 2024-03-14 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0413_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='medico_chamadas_contabilizadas',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='triagem',
            name='medico_respondeu_ao_chamado',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Aguardando', 'Aguardando'), ('Liberado', 'Liberado'), ('Em atendimento', 'Em atendimento')], default='Aguardando', max_length=30, null=True),
        ),
    ]
