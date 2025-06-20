# Generated by Django 4.1.4 on 2023-03-16 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Medicos', '0016_salas_atendimento'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroSala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_Sala', models.CharField(max_length=40)),
                ('descricao_Sala', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='salas_atendimento',
            name='nomeSala',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Medicos.cadastrosala'),
        ),
    ]
