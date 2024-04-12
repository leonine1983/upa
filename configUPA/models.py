import os
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField


# Create your models here.
class config_Marquee(models.Model):
    gif_medico = models.BooleanField(null=False, default=False)
    gif_enfermera = models.BooleanField(null=False, default=False)
    gif_Ze_gotina = models.BooleanField(null=False, default=False)
    data_ativa = models.BooleanField(null=False, default=True)
    hora_ativa = models.BooleanField(null=False, default=True)
    distancia = models.IntegerField(null=False, default='60' )
    bem_vindo_ativa = models.BooleanField(null=False, default=True)
    bem_vindo_ativa_coracao = models.BooleanField(null=False, default=True)    
    bem_vindo_msg = models.TextField(null=False, default="Bem vindos à UPA de Vera Cruz ")
    mensagem_ativa = models.BooleanField(null=False, default=True)
    mensagem = models.TextField(null=True, default="🌞 Agradecemos pela paciência e confiança. Pedimos que aguardem com tranquilidade, pois estamos preparando tudo para atendê-los da melhor forma possível. Em breve, cada um de vocês será chamado para receber o cuidado especial que merece. Tenham um dia maravilhoso! 💙")
    letreiro_ativa = models.BooleanField(null=False, default=True)

    def __str__(self) :
        return self.mensagem


class Video_Backgroud_Painel(models.Model):
    title = models.CharField(max_length=100, null=True)
    dataHora = models.DateTimeField(auto_now=True)
    video_file = models.FileField(upload_to='videos/', null=True)

    class Meta:
        ordering = ['-dataHora']

    #Criar o metodo delete para apagar os arquivos de video relacionados aos registros presentes no model
    def delete(self, *args, **kwargs):
        #Remove os arquivo de video realiconado
        if self.video_file:
            video_file_path = os.path.join(settings.MEDIA_ROOT, self.video_file.name)
            if os.path.isfile(video_file_path):
                os.remove(video_file_path)

        super().delete(*args)

    def __str__(self):
        return self.title

class Notificate_system(models.Model):
    user = models.ForeignKey (User, related_name='controle_notificacao', on_delete=models.CASCADE, null=True)
    date = models.DateField(auto_now_add=True)
    
    name = models.TextField(max_length=100, default='Atualização de fim de ano')
    description = RichTextField(max_length=500, null=False, default='', verbose_name='Descrever a atualização')
    visto = models.BooleanField(default=False)

    def __str__(self):
        return self.description
