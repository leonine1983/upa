# Generated by Django 4.1.4 on 2022-12-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='nome_social',
            field=models.CharField(default='nome_social', max_length=50),
        ),
    ]
