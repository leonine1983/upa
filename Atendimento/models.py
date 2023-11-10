from datetime import date, datetime

#criar o grupos para restringir o acesso dos usuarios
from django.contrib.auth.models import Group, Permission
from django.db import models

# Após rodar o migrate alguns dados precisam ser lançados no sistema
from django.db.models.signals import post_migrate
from django.dispatch import receiver
import random
import uuid


class Bairro (models.Model):
    bairro_nome = models.CharField(max_length=30)

    @receiver(post_migrate)
    def create_bairro(sender, **kwargs):
        bairro_nome = ['Aratuba', 'Baiacu', 'Barra do Gil', 'Barra do Pote', 'Berlinque', 'Cacha Pregos', 'Catu', 'Conceição', 'Coroa', 'Gameleira', 'Ilhota', 'Jiribatuba', 'Mar Grande', 'Ponta Grossa', 'Riachinho', 'Tairu']
    
        if not Bairro.objects.exists():
            for b in bairro_nome:
                Bairro.objects.create(
                    bairro_nome = b
                )

    def __str__(self):
        return self.bairro_nome
    
        
class Rua(models.Model):
    rua_nome = models.CharField(max_length=100)

    @receiver(post_migrate)
    def create_rua(sender, **kwargs):
        rua_nome = ['Av. Ernesto Carneiro Ribeiro']
    
        if not Rua.objects.exists():
            for b in rua_nome:
                Rua.objects.create(
                    rua_nome = b
                )

    def __str__(self):
        return self.rua_nome
    

class Cidade(models.Model):
    cidade = models.CharField(max_length=100)

    @receiver(post_migrate)
    def create_cidade(sender, **kwargs):    
        if not Cidade.objects.exists():
            Cidade.objects.create(
                    cidade = "Vera Cruz"
                )

    def __str__(self):
        return self.cidade
    
    
class Estado(models.Model):
    estado = models.CharField(max_length=100)

    @receiver(post_migrate)
    def create_estado(sender, **kwargs):    
        if not Estado.objects.exists():
            Estado.objects.create(
                estado = 'Bahia'
            )

    def __str__(self):
        return self.estado
    

class Pais(models.Model):
    pais = models.CharField(max_length=100)

    @receiver(post_migrate)
    def create_pais(sender, **kwargs):    
        if not Pais.objects.exists():
            Pais.objects.create(
                pais = 'Brasil'
            )

    def __str__(self):
        return self.pais


class genero_sexual(models.Model):
    nome_genero = models.CharField(max_length=40, null=False, default='Outros')    

    @receiver(post_migrate)
    def create_genero_sexual(sender, **kwargs):
        #Irá pecorrer a lista de generos sexuais e adicionar conteudo nessa lista caso não exista
        nome_genero = ['Masculino', 'Feminino', 'Não-binário', 'Gênero fluido', 'Agênero', 'Dois-espíritos']
        if not genero_sexual.objects.exists():
            for gn in nome_genero:
                genero_sexual.objects.create(
                    nome_genero = gn
                    )
                print(f'generos: {nome_genero}')

    def __str__(self):
        return self.nome_genero
    

class Etnia(models.Model):
    etnia = models.CharField(max_length=40, null=False, default='Outros')    

    @receiver(post_migrate)
    def create_etnia(sender, **kwargs):
        #Irá pecorrer a lista de generos sexuais e adicionar conteudo nessa lista caso não exista
        etnia= ['Negro', 'Pardo', 'Branco']
        if not Etnia.objects.exists():
            for gn in etnia:
                Etnia.objects.create(
                    etnia = gn
                    )

    def __str__(self):
        return self.etnia


class ficha_de_atendimento(models.Model):
    nome_social = models.CharField(max_length=40, null=False, default='')
    codigo_pacient = models.CharField(max_length=8, null=True, verbose_name="Código do paciente")
    idade = models.IntegerField(null=False, default='00')    
    etnia = models.ForeignKey(Etnia, null=True, on_delete=models.CASCADE)
    data_nascimento = models.DateField( auto_now=False, auto_now_add=False, default='')
    sexo = models.ForeignKey(genero_sexual, null=True, on_delete=models.CASCADE)
    RG = models.CharField(max_length=13, null=False, default='000.000.00-00')
    CPF = models.CharField(max_length=14, null=False, default='000.000.000-00')
    nacionalidade = models.CharField(max_length=30, null=False, default='')
    rua = models.ForeignKey(Rua, null=True, on_delete=models.PROTECT)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name='fichas_atendimento_bairro')
    cidade = models.ForeignKey(Cidade, null=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, null=True, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='fichas_atendimento_pais')
    CEP = models.CharField(max_length=9, null=False, default='')
    nome_mae = models.CharField(max_length=40, null=False, default='')
    responsavel = models.CharField(max_length=30, null=True)
    tel = models.CharField(max_length=16, null=False, default='')
    data_cadastro = models.DateField(auto_now_add=True, null=False)
    horario_cadastro = models.TimeField(null=True, auto_now_add=True)
    cartao_sus = models.CharField(max_length=15, null=True)
    ultimo_pk = None
    choices=(      
        ('0', 'Não'),
        ('1','Sim'),
    )
    alergias = models.CharField(max_length=3, default=2, choices= choices, )
    conteudo_alergia = models.TextField(max_length=500, null=True, blank=True, default='Não possui alergias (Para tornar editável essa área, é necessário informar que o paciente possui alergias)')
    comorbidades = models.CharField(max_length=3, default=2, choices= choices )
    conteudo_comorbidades = models.TextField(max_length=500, null=True, blank=True, default='Não possui comobirdades (Para tornar editável essa área, é necessário informar que o paciente possui comobirdades)')
    
    class Meta:
        ordering = ['-data_cadastro']

   
    
    def save(self, *args, **kwargs):
        
        today = date.today()
        self.idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        super().save(*args, **kwargs)
        return self.pk
        
    def __str__ (self):
        return self.nome_social


class envio_triagem(models.Model):
    paciente_envio_triagem = models.ForeignKey(ficha_de_atendimento, related_name='rel_ficha_atendimento', null=False, on_delete=models.PROTECT)   
    data_envio_triagem = models.DateField(auto_now_add=True, null=True)
    horario_triagem = models.TimeField(auto_now_add=True, null=True)
    TRIAGEM_CHOICES = (
        ("1", "Sim"),
        ("0", "Não")
    )
    triagem_concluida = models.CharField(max_length=1, null=True)
    data_triagem_concluida = models.DateField(auto_now=True, null=True)
    q1 = models.CharField(max_length=1, null=True, default='')
    q2 = models.CharField(max_length=1, null=True, default='')
    q3 = models.CharField(max_length=1, null=True, default='')
    q4 = models.CharField(max_length=1, null=True, default='')
    q5 = models.CharField(max_length=1, null=True, default='')
    q6 = models.CharField(max_length=1, null=True, default='')
    q7 = models.CharField(max_length=1, null=True, default='')
    q8 = models.CharField(max_length=1, null=True, default='')
    q9 = models.CharField(max_length=1, null=True, default='')    

    class Meta:
        ordering = ['horario_triagem', 'data_envio_triagem']
        permissions = [('Acesso_permitido_envio_Tri', 'Acesso permitido para envio à Fila de Triagem')]

    def __str__ (self):
        return '{}'.format(self.paciente_envio_triagem)

