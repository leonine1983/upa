# Generated by Django 4.2 on 2023-07-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0096_remove_triagem_atend_especializado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('2', 'Liberado'), ('1', 'Em atendimento'), ('0', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
    ]
