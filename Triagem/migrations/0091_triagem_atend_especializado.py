# Generated by Django 4.2 on 2023-07-09 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0090_alter_atendimento_especializado_situacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='atend_especializado',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Triagem.atendimento_especializado'),
        ),
    ]