# Generated by Django 4.2.7 on 2024-03-04 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0296_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Aguardando', 'Aguardando'), ('Em atendimento', 'Em atendimento'), ('Liberado', 'Liberado')], default='Aguardando', max_length=30, null=True),
        ),
    ]