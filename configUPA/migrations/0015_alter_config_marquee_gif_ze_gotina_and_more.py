# Generated by Django 4.2.7 on 2023-12-11 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configUPA', '0014_alter_video_backgroud_painel_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config_marquee',
            name='gif_Ze_gotina',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='config_marquee',
            name='gif_enfermera',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='config_marquee',
            name='gif_medico',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='config_marquee',
            name='mensagem',
            field=models.TextField(default='🌞 Agradecemos pela paciência e confiança. Pedimos que aguardem com tranquilidade, pois estamos preparando tudo para atendê-los da melhor forma possível. Em breve, cada um de vocês será chamado para receber o cuidado especial que merece. Tenham um dia maravilhoso! 💙', null=True),
        ),
    ]
