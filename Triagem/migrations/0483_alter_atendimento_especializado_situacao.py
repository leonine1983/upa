# Generated by Django 4.2.7 on 2024-04-22 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0482_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Liberado', 'Liberado'), ('Aguardando', 'Aguardando'), ('Em atendimento', 'Em atendimento')], default='Aguardando', max_length=30, null=True),
        ),
    ]