# Generated by Django 4.2.7 on 2023-12-01 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0165_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Aguardando', 'Aguardando'), ('Em atendimento', 'Em atendimento'), ('Liberado', 'Liberado')], default='Aguardando', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='atestado',
            field=models.CharField(blank=True, default='0', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='encaminhamento',
            field=models.TextField(blank=True, default='Digite o encaminhamento do paciente', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='exames',
            field=models.ManyToManyField(blank=True, null=True, to='Triagem.exames_model'),
        ),
    ]
