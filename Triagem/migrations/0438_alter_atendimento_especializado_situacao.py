# Generated by Django 4.2.7 on 2024-03-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0437_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Liberado', 'Liberado'), ('Em atendimento', 'Em atendimento'), ('Aguardando', 'Aguardando')], default='Aguardando', max_length=30, null=True),
        ),
    ]