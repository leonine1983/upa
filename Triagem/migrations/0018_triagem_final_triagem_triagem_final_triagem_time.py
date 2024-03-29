# Generated by Django 4.1.4 on 2023-01-10 00:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0017_alter_triagem_paciente_triagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='final_triagem',
            field=models.CharField(choices=[('0', 'Não'), ('1', 'Sim')], default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triagem',
            name='final_triagem_time',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
