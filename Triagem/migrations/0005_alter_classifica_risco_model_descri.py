# Generated by Django 4.1.4 on 2022-12-19 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0004_alter_classifica_risco_model_descri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classifica_risco_model',
            name='descri',
            field=models.CharField(default='', max_length=500, verbose_name='Descrição'),
        ),
    ]
