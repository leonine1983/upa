# Generated by Django 4.2.7 on 2024-03-01 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0088_alter_ficha_de_atendimento_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ficha_de_atendimento',
            options={'ordering': ['nome_social']},
        ),
    ]