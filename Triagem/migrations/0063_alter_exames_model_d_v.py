# Generated by Django 4.2 on 2023-04-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0062_exames_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exames_model',
            name='d_v',
            field=models.IntegerField(max_length=1, null=True),
        ),
    ]