from django.db import models

# Create your models here.
class config_Marquee(models.Model):
    gif_medico = models.BooleanField(null=False, default=True)
    gif_enfermera = models.BooleanField(null=False, default=True)
    gif_Ze_gotina = models.BooleanField(null=False, default=True)
    data_ativa = models.BooleanField(null=False, default=True)
    hora_ativa = models.BooleanField(null=False, default=True)
    distancia = models.IntegerField(null=False, default='60' )
    bem_vindo_ativa = models.BooleanField(null=False, default=True)
    bem_vindo_ativa_coracao = models.BooleanField(null=False, default=True)    
    bem_vindo_msg = models.TextField(null=False, default="Bem vindos à UPA de Vera Cruz ")
    mensagem_ativa = models.BooleanField(null=False, default=True)
    mensagem = models.TextField(null=True, default="")
    letreiro_ativa = models.BooleanField(null=False, default=True)

    def __str__(self) :
        return self.mensagem


class Video_Backgroud_Painel(models.Model):
    title = models.CharField(max_length=100)
    dataHora = models.DateTimeField(auto_now=True)
    video_file = models.FileField(upload_to='videos/')

    class Meta:
        ordering = ['-dataHora']

    def __str__(self):
        return self.title

