# Generated by Django 4.2.7 on 2023-12-31 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0223_remove_triagem_preescrever_medicamento_medico_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Em atendimento', 'Em atendimento'), ('Aguardando', 'Aguardando'), ('Liberado', 'Liberado')], default='Aguardando', max_length=30, null=True),
        ),
    ]
