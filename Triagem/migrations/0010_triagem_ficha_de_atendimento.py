# Generated by Django 4.1.4 on 2023-01-02 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0012_alter_envio_triagem_paciente'),
        ('Triagem', '0009_alter_triagem_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='ficha_de_atendimento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='Atendimento.ficha_de_atendimento'),
            preserve_default=False,
        ),
    ]
