# Generated by Django 4.2 on 2023-04-28 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0069_remove_triagem_exames_triagem_exames'),
    ]

    operations = [
        migrations.AddField(
            model_name='triagem',
            name='alergias',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='triagem',
            name='conteudo_alergia',
            field=models.TextField(max_length=300, null=True),
        ),
    ]