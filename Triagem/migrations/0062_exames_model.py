# Generated by Django 4.2 on 2023-04-18 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0061_alter_triagem_atestado'),
    ]

    operations = [
        migrations.CreateModel(
            name='exames_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procedimento', models.IntegerField(max_length=5, null=True)),
                ('classificacao', models.CharField(max_length=12, null=True)),
                ('d_v', models.ImageField(max_length=1, null=True, upload_to='')),
                ('descricao', models.CharField(max_length=50, null=True)),
                ('valor', models.CharField(max_length=10, null=True)),
            ],
        ),
    ]