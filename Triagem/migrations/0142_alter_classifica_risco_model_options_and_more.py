# Generated by Django 4.2.7 on 2023-11-17 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0141_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classifica_risco_model',
            options={'ordering': ['-id']},
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Liberado', 'Liberado'), ('Em atendimento', 'Em atendimento'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
    ]