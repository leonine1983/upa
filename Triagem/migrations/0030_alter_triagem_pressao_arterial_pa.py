# Generated by Django 4.1.4 on 2023-01-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0029_alter_triagem_enviar_ambulatorio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='pressao_arterial_PA',
            field=models.CharField(default='', help_text='120x80 mmHg', max_length=11),
        ),
    ]
