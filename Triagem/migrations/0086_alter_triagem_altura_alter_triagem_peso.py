# Generated by Django 4.2 on 2023-06-21 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0085_triagem_altura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='triagem',
            name='altura',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='triagem',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
