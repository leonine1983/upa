from datetime import date, datetime

#criar o grupos para restringir o acesso dos usuarios
from django.contrib.auth.models import Group, Permission
from django.db import models

#Restrição


# Create your models here.

"""
Group.objects.create(name='UPA-Admin')
Group.objects.create(name='Medicos')
Group.objects.create(name='Enfermagem')
Group.objects.create(name='Tec_Enfermagem')"""

#Cria os grupos
#Associa as permissões aos grupos correspondentes:

upaAdmin_group = Group.objects.get(name = 'group_UPA-Admin')
medico_group = Group.objects.get(name='group_Medicos')
enfermagem_group = Group.objects.get(name = 'group_Enfermagem')
tecEnfermagem_group = Group.objects.get (name = 'group_Tec_Enfermagem')



class genero_sexual(models.Model):

    #class Meta:
        #permissions = [('Acesso_permitido_Admin', 'Acesso permitido ao admin do sistema na UPA')]

    nome_genero = models.CharField(max_length=40, null=False, default='Outros')    

    def __str__(self):
        return self.nome_genero


class ficha_de_atendimento(models.Model):
    nome_social = models.CharField(max_length=40, null=False, default='')
    idade = models.IntegerField(null=False, default='00')
    data_nascimento = models.DateField( auto_now=False, auto_now_add=False, default='')
    sexo = models.ForeignKey(genero_sexual, null=True, on_delete=models.PROTECT)
    RG = models.CharField(max_length=13, null=False, default='000.000.00-00')
    CPF = models.CharField(max_length=14, null=False, default='000.000.000-00')
    nacionalidade = models.CharField(max_length=30, null=False, default='')
    rua = models.CharField(max_length=50, null=False, default='')
    bairro = models.CharField(max_length=30, null=False, default='')
    cidade = models.CharField(max_length=30, null=False, default='')
    estado = models.CharField(max_length=30, null=False, default='')
    CEP = models.CharField(max_length=9, null=False, default='')
    nome_mae = models.CharField(max_length=40, null=False, default='')
    responsavel = models.CharField(max_length=30, null=True)
    tel = models.CharField(max_length=16, null=False, default='')
    data_cadastro = models.DateField(auto_now_add=True, null=False)
    horario_cadastro = models.TimeField(null=True, auto_now_add=True)
    cartao_sus = models.CharField(max_length=15, null=True)
    ultimo_pk = None

    
    class Meta:
        ordering = ['-data_cadastro']

    def save(self, *args, **kwargs):
        # Calcula a idade do paciente
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
    data_triagem_concluida = models.DateField(auto_now_add=True, null=True)
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


# Para recuperar dados da sessão do usuario
def login(request):
    username = request.POST['username']
    request.session['username'] = username
    # ...

# Para recuperar o nome do usuário da sessão em uma página posterior
def profile(request):
    username = request.session.get('username', None)
    if username is None:
        # redirecionar para a página de login
        return redirect('login')








        






