# Generated by Django 4.2 on 2023-07-15 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0117_triagem_pressao_arterial_pa_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Em atendimento', 'Em atendimento'), ('Liberado', 'Liberado'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='pressao_arterial_PA',
            field=models.FloatField(blank=True, null=True, verbose_name='Pressão arterial minima PA-1'),
        ),
    ]
