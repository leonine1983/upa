# Generated by Django 4.2.7 on 2024-03-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Triagem', '0421_remove_triagem_medico_respondeu_ao_chamado_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='triagem',
            old_name='medico_respondeu_chamado',
            new_name='medico_respondeu_ao_chamado',
        ),
        migrations.AddField(
            model_name='triagem',
            name='respondeu_ao_chamado_medico',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='atendimento_especializado',
            name='situacao',
            field=models.CharField(choices=[('Aguardando', 'Aguardando'), ('Em atendimento', 'Em atendimento'), ('Liberado', 'Liberado')], default='Aguardando', max_length=30, null=True),
        ),
    ]
