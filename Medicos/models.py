#Para criar outros campos para o usuario
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin, User)
from django.db import models

from Atendimento.models import *
from Triagem.models import triagem
from django.db.models import Q


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser definido')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telefone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    endereco = models.CharField(max_length=255)
    crm = models.CharField(max_length=13, null=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_user_permissions')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='custom_user')
    grupo = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='custom_users')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.email



# -----------------Controle de doenças CID 10 ---------------------------
class cid_10 (models.Model):
    codigo = models.CharField(max_length=12, null=True)
    descricao = models.TextField(max_length=300, null=True)
    codigo_Cid10 = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    

    @staticmethod
    def consulta_personalizada(q):
        return cid_10.objects.filter(Q(codigo=q) | Q(descricao_icontains=q) | Q(codigo_Cid10 =q) )
    








# Create your models here.
class Medico_atendimento (models.Model):
    paciente_medico_atendimento = models.ForeignKey(triagem, null=False, on_delete=models.PROTECT)    
    historico_doenca_atual_HDA = models.TextField(max_length=500, null=True, default='Não se aplica')
    exame_fisico = models.TextField(max_length=500, null=True, default='Não se aplica')
    Diagnostico = models.CharField(max_length=200, null=True, default='Não se aplica')
    classificacao_internacional_doenca_CID = models.ForeignKey(cid_10, null=True, default='Não se aplica', on_delete=models.CASCADE)
    conduta = models.TextField(max_length=500, null=True, default='Não se aplica')
    data_medico = models.DateField(auto_now_add=True, null=False)
    hora_medico = models.TimeField(auto_now_add=True, null=True )
    tempo_espera_paciente = models.DurationField(blank=True, null=True)
    #alergias = (
     #   ('sim','Sim'),
      #  ('nao', 'Não'),
    #)
    #alergia_sim = models.TextField(max_length=300, null=True)
    #alta = (
     #   ('Sim'),
      #  ('Não'),
    #)
    medico_nome = models.CharField(max_length=40, null=True)

    # Nessa classe Meta será criado as permissões
    
    class Meta:
        permissions = [('Acesso_permitido_Admin', 'Acesso permitido ao admin do sistema na UPA'),\
                       ('Acesso_permitido_medic', 'Acesso permitido aos médicos') ]




# CRIAR O MODEL USUARIOS --------------------------------------------------

# CRIAR O MODEL USUARIOS --------------------------------------------------


from django.contrib.auth.models import User
# models.py
from django.db import models
from django.utils import timezone


class Chamar_P_para_atendimento(models.Model):
    # Define o modelo "Chamar_P_para_atendimento" com três campos: "nome_paciente", "profissionalSaude" e "data_chamada"
    nome_paciente = models.CharField(max_length=100)
    profissionalSaude_id = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    data_chamada = models.DateTimeField(auto_now=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    data_atualizacao = models.DateTimeField(default=timezone.now)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(Chamar_P_para_atendimento, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):

        if self.request and self.request.user:
            # Define a data e hora de criação do registro
            self.data_criacao = timezone.now()
            self.profissionalSaude_id = self.request.user

            # Exclui os últimos 5 registros criados pelo usuário
            Chamar_P_para_atendimento.objects.all().delete()            

        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.nome_paciente


class CadastroSala(models.Model):
    nome_Sala = models.CharField(max_length=40, null=False, verbose_name='Escreva o nome da sala. Ex: Sala 01')
    descricao_Sala = models.TextField(max_length=200, null=False, verbose_name='Descreva a ulitilização da sala. Ex.: Sala de atendimento pediátrico')

    def __str__(self):
        return self.nome_Sala


class Salas_Atendimento(models.Model):
    nomeSala = models.OneToOneField(CadastroSala, on_delete=models.CASCADE)
    profissionalSaude = models.ForeignKey(User, limit_choices_to={'groups__name__in':['group_Medicos', 'group_Enfermagem']}, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.nomeSala)
    






   


    

