# Generated by Django 4.2 on 2023-04-14 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configUPA', '0011_video_backgroud_painel'),
    ]

    operations = [
        migrations.AddField(
            model_name='video_backgroud_painel',
            name='dataHora',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
