# Generated by Django 4.1.4 on 2023-01-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atendimento', '0017_alter_envio_triagem_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='envio_triagem',
            name='data_triagem_concluida',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='envio_triagem',
            name='triagem_concluida',
            field=models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=1, null=True),
        ),
    ]
