# Generated by Django 4.2 on 2023-05-09 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0080_alter_triagem_exames'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='nome_da_enfermeira',
            field=models.CharField(default='', max_length=50),
        ),
    ]
