# Generated by Django 4.2.7 on 2024-03-14 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0095_ficha_de_atendimento_nome_completo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio_triagem',
            name='nome_recepcionista',
            field=models.CharField(default='', max_length=40, null=True),
        ),
    ]
