# Generated by Django 4.1.4 on 2022-12-31 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0008_alter_classifica_risco_model_classifica_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='triagem',
            options={'ordering': ['classifica_tipo']},
        ),
        migrations.AlterField(
            model_name='classifica_risco_model',
            name='descri',
            field=models.TextField(default='', max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='pressao_arterial_PA',
            field=models.CharField(default='mmHg', max_length=11, null=True),
        ),
    ]
