# Generated by Django 4.2 on 2023-07-09 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0035_ficha_de_atendimento_alergias_and_more'),
        ('Triagem', '0088_tipos_atendimento_atendimento_especializado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('1', 'Em atendimento'), ('0', 'Aguardando'), ('2', 'Liberado')], max_length=30),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='paciente_triagem',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='rel_envio_triagem', to='Atendimento.envio_triagem'),
        ),
    ]