# Generated by Django 4.2 on 2023-04-24 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0032_remove_ficha_de_atendimento_rua'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_de_atendimento',
            name='rua',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='Atendimento.rua'),
        ),
    ]
