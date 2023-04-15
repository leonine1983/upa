from django.db import models
from django.utils import timezone

from Atendimento.models import envio_triagem, ficha_de_atendimento


class Classifica_risco_model(models.Model):

    classifica_tipo = models.CharField(max_length=30, null=False, default="Vermelho", verbose_name="Tipo de Emergência")
    descri = models.TextField(max_length=500, null=False, default='', verbose_name='Descrição')

    class Meta:
        ordering = ['-classifica_tipo']        
        #permissions = [('Acesso_permitido_Admin', 'Acesso permitido ao admin do sistema na UPA')\
        #                ('Acesso_permitido_medic', 'Acesso permitido aos médicos'),\
        #                 ('Acesso_permitido_Enfer', 'Acesso permitido aos enfermeiros')]

    def __str__(self) -> str:
        return self.classifica_tipo





# Create your models here.
class triagem (models.Model):
    paciente_triagem = models.ForeignKey(envio_triagem, related_name='rel_envio_triagem', null=False, on_delete=models.PROTECT)        
    pressao_arterial_PA = models.CharField(max_length=11, null=False, default='')
    frequencia_cardiaca_FC = models.CharField(max_length=7, null=False, default='')
    frequencia_respiratoria_FR = models.CharField(max_length=6, null=False, default='')
    saturacao_de_oxigenio_SPO2 = models.CharField(max_length=3, null=False, default='')
    hemoglicoteste_HGT = models.CharField(max_length=9, null=False, default='')
    temperatura_TEMP = models.CharField(max_length=7, null=False, default='')
    peso = models.CharField(max_length=6, null=False, default='')    
    data_triagem = models.DateField(auto_now_add=True, null=False)
    hora_triagem = models.TimeField(auto_now_add=True, null=True )
    classifica_tipo = models.ForeignKey(Classifica_risco_model, null=True, on_delete=models.PROTECT, verbose_name='Classificação de Emergência')
    observacao = models.TextField(max_length=700, null=False, verbose_name='Observação')
    choices=(
        ('1','Sim'),
        ('0', 'Não')
    )
    
    preescrever_medicamento_medico = models.TextField(max_length=500, null=True, default='Preescreva o medicamento para o paciente')
    encaminhamento = models.TextField(max_length=500, null=True, default='Digite o encaminhamento do paciente')
    atestado = models.TextField(max_length=15, null=True, default='Digite a quantidade de dias que o paciente irá ficar de repouso')
    exames = models.TextField(max_length=500, null=True, default='Preencha com a relação de exames')
    
    enviar_ambulatorio = models.CharField(max_length=3, choices=choices, null=False) 
    final_triagem = models.CharField(max_length=3, null=True, default='')
    final_triagem_time = models.DateField(auto_now_add=True, null=False)
    final_medico_atendimento = models.CharField(max_length=3, null=True, default='')
    nome_da_enfermeira = models.CharField(max_length=20, null=False, default='')

    class Meta:
        ordering = ['classifica_tipo', 'hora_triagem', 'paciente_triagem__paciente_envio_triagem__idade']    

    def __str__ (self):
        return '{}'.format(self.paciente_triagem)


class ChamarPaciente(models.Model):
    id_paciente = models.CharField(max_length=255)
    nome_paciente = models.CharField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        """Sobrescreve o método 'save' padrão do django para adicionar a lógica de negócio.
        Essa função será chamada toda as vezes qeu um objeto desse modelo for salvo no banco de dados."""

        #exclui os registros existentes
        ChamarPaciente.objects.all().delete()

        #define a data e hora da criação do registro
        self.data_criacao = timezone.now()

        #salva o registro no banco de dados
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome_paciente

# xxxxxxxxxxxxxxxxxxxxxxxxxxxx CADASTRA E ALTERA USUARIOS xxxxxxxxxxxxxxxxxxxxxxxxxx

#Para criar outros campos para o usuario

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, telefone=None, data_nascimento=None, coren=None, rua=None, bairro=None, cidade=None, cep=None):
        if not email:
            raise ValueError('Os usuários devem ter um endereço de email')

        user = self.model(
            email=self.normalize_email(email),
            telefone=telefone,
            data_nascimento=data_nascimento,
            coren=coren,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, telefone=None, data_nascimento=None, coren=None, rua=None, bairro=None, cidade=None, cep=None):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            telefone=telefone,
            data_nascimento=data_nascimento,
            coren=coren,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Definindo um gerenciador de usuários customizado que herda da classe BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User

class CustomUserManager(BaseUserManager):
    
    def create_user(self, username, email, password=None, telefone=None, data_nascimento=None, coren=None, rua=None, bairro=None, cidade=None, cep=None):
        
        if not email:
            raise ValueError('Os usuários devem ter um endereço de email')
        
        user = self.model(
            email=self.normalize_email(email),
            telefone=telefone,
            data_nascimento=data_nascimento,
            coren=coren,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
            username=username
        )

        user.set_password(password)
        
        user.save(using=self._db)
        
        # Cria um usuário no modelo User do Django
        user_django = User.objects.create_user(username=email, email=email, password=password)

        # Atribui o campo user do modelo CustomUserTriagem ao modelo User do Django
        user.user = user_django

        # Salva o usuário no banco de dados
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password=None, telefone=None, data_nascimento=None, coren=None, rua=None, bairro=None, cidade=None, cep=None):
        
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
            telefone=telefone,
            data_nascimento=data_nascimento,
            coren=coren,
            rua=rua,
            bairro=bairro,
            cidade=cidade,
            cep=cep,
        )
        
        user.is_admin = True
        
        user.save(using=self._db)
        
        # Cria um usuário no modelo User do Django
        user_django = User.objects.create_superuser(username=email, email=email, password=password)

        # Atribui o campo user do modelo CustomUserTriagem ao modelo User do Django
        user.user = user_django

        # Salva o usuário no banco de dados
        user.save(using=self._db)

        return user

class CustomUserTriagem(AbstractBaseUser):

    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField(null=True, blank=True)
    coren = models.CharField(max_length=20)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    cep = models.CharField(max_length=10)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    # adicionando um campo user que referencia o modelo User do Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # definindo o campo que será usado para autenticação do usuário (username)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', 'telefone', 'data_nascimento', 'coren', 'rua', 'bairro', 'cidade', 'cep']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True






