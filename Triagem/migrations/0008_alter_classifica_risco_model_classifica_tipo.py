# Generated by Django 4.1.4 on 2022-12-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0007_alter_classifica_risco_model_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifica_risco_model',
            name='classifica_tipo',
            field=models.CharField(default='Vermelho', max_length=30, verbose_name='Tipo de Emergência'),
        ),
    ]
