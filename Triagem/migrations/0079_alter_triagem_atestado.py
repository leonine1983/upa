# Generated by Django 4.2 on 2023-05-08 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0078_remove_triagem_alergias_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='atestado',
            field=models.CharField(default='0', max_length=2, null=True),
        ),
    ]
