# Generated by Django 4.2.7 on 2023-12-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0068_alter_ficha_de_atendimento_conteudo_alergia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='conteudo_alergia',
            field=models.TextField(blank=True, default='Não possui alergias (Para tornar editável essa área, é necessário informar que o paciente possui alergias)', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_de_atendimento',
            name='conteudo_comorbidades',
            field=models.TextField(blank=True, default='Não possui comobirdades (Para tornar editável essa área, é necessário informar que o paciente possui comobirdades)', max_length=500, null=True),
        ),
    ]