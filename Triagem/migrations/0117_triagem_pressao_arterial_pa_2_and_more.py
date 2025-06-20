# Generated by Django 4.2 on 2023-07-15 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0116_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='pressao_arterial_PA_2',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Liberado', 'Liberado'), ('Aguardando', 'Aguardando'), ('Em atendimento', 'Em atendimento')], default='Aguardando', max_length=30, null=True),
        ),
    ]
