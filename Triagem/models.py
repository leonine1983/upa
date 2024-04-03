from django.db import models
# libs executadas para no pos migrate
from django.db.models.signals import post_migrate, post_save
from django.db.models import Case, When, Value, BooleanField
from Atendimento.models import Priority
from django.dispatch import receiver
from Atendimento.models import envio_triagem
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, User
from ckeditor.fields import RichTextField

class Classifica_risco_model(models.Model):
    classifica_tipo = models.CharField(max_length=30, null=False, default="Vermelho", verbose_name="Tipo de Emergência")
    descri = models.TextField(max_length=500, null=False, default='', verbose_name='Descrição')

    class Meta:
        ordering = ['id']     

    @receiver(post_migrate)
    def create_classifica_risco(sender, **kwargs):
        # Irá pecorrer a lista de riscos e adicionar conteudo caso não exista
        groups_risco = ['Vermelho', 'Laranja','Amarelo', 'Verde', 'Azul']       
        groups_descri = [
                        'Emergência imediata: Atendimento médico imediato é necessário. O paciente está em risco de vida.',
                        'Emergência: Atendimento médico é urgente, mas não imediatamente para salvar a vida.',
                        'Urgência: O paciente precisa de atendimento, mas pode esperar um pouco. Não há risco imediato de vida.',
                        'Semi-urgência: O paciente precisa de atendimento, mas pode esperar mais tempo. Não há risco significativo de vida.',
                        'Não urgente: O paciente precisa de atendimento, mas pode esperar. Não há risco significativo de vida.',
                        'Nao_Respondeu: Classificação para pacientes que não responderam ao chamado para a classificação'
                    ]
        
        if not Classifica_risco_model.objects.exists():
            for i in range(len(groups_risco)):
                Classifica_risco_model.objects.create(
                    classifica_tipo=groups_risco[i],
                    descri=groups_descri[i]
                )        
        
        if not Classifica_risco_model.objects.exists():
            for ris in groups_risco:
                for des in groups_descri:
                    Classifica_risco_model.objects.create(
                        classifica_tipo = ris,
                        descri = des
                    )    
    
    def __str__(self) -> str:
        return self.classifica_tipo
    

# EXAMES
class Exames_Model(models.Model):
    # procedimento = models.IntegerField(max_length=5, null=True)
    # classificacao = models.CharField(max_length=12, null=True)
    # d_v = models.IntegerField(max_length=1, null=True)
    # descricao = models.CharField(max_length=50, null=True)
    # valor = models.CharField(max_length=10, null=True)
    nome_exame = models.CharField(max_length=50, null=False, default='Nenhuma solicitação de exame')
    # caso não exista registros no model exames, 
    # o seguinte metodo deverá ser executado
    @receiver(post_migrate)
    def create_exames_Model(sender, **kwargs):
        lista_exames_padrao = ['Nenhum', 'HEMOGRAMA', 'PLAQUETAS', 'GRUPO SANGUÍNEO',\
     'FATO RH', 'TS', 'TC', 'TP', 'TTPA', 'PL',\
         'RC', 'HB GLICOSILADA', 'VHS', 'TGO', 'TGP',\
             'GAMA GT', 'UREIA', 'CREATINA', 'BILIRRUBINA TOTAL',\
                 'GLICOSE', 'GPP', 'FERRO', 'SÓDIO', 'POTÁSSIO', 'COLESTEROL T',\
                     'HDL', 'LDL', 'VLDL', 'TRIGLICERIDEOS', 'AC. ÚRICO', 'CK',\
                         'CK-MB', 'Ca', 'Mg', 'FÓSFORO', 'AMILASE', 'PROTEÍNAS TOTAIS',\
                             'ALB', 'GLOBULINA', 'MAGNÉSIO', 'CLORO', 'CPK', 'FOSFATASE ALCALINA',\
                                 'PCR', 'AGHBS', 'ANTIHCV', 'HIV', 'VDRL', 'ASLO', 'BHCG URINÁRIO',\
                                     'BHCG SÉRICO', 'LÁTEX', 'SUMÁRIO DE URINA', 'P. DE FEZES']
        if not Exames_Model.objects.exists():
            for exame in lista_exames_padrao:
                Exames_Model.objects.create(                    
                    nome_exame = exame
                )

    def __str__(self):
        return self.nome_exame


# Cria tipos de atendimentos
class Tipos_Atendimento(models.Model):
    nome = models.CharField(max_length=30, null=False)

    @receiver(post_migrate)
    def registros_tipos_atendimentos(sender, **kwargs):
        if not Tipos_Atendimento.objects.exists():
            Tipos_Atendimento.objects.create(
                nome = "Raio X"
            )
    
    def __str__(self):
        return self.nome
        
    
class TriagemManager(models.Manager):
    def get_queryset(self):
        priority_patients = Priority.objects.values_list('nome_priority__id', flat=True)
        queryset = super().get_queryset().annotate(
            is_priority = Case(
                When(paciente_triagem__paciente_envio_triagem__id__in=priority_patients, then=Value(True)),
                default=Value(False),
                output_field=BooleanField()
            )
        ).order_by('classifica_tipo','is_priority', 'hora_triagem', 'paciente_triagem__paciente_envio_triagem__idade')

        return queryset
    

class triagem(models.Model):
    paciente_triagem = models.OneToOneField(envio_triagem, related_name='rel_envio_triagem', null=False, on_delete=models.PROTECT)
    passou_por_atend_medico = models.BooleanField(default=False, null=True)
    exames = models.ManyToManyField(Exames_Model, blank=True)
    pressao_arterial_PA = models.FloatField(null=True, blank=True, verbose_name='Pressão arterial (mínima) PA-1')
    pressao_arterial_PA_2 = models.FloatField(null=True, blank=True, verbose_name='Pressão arterial (máxima) PA-2')
    frequencia_cardiaca_FC = models.FloatField(null=True, blank=True)
    frequencia_respiratoria_FR = models.FloatField(null=True, blank=True)
    saturacao_de_oxigenio_SPO2 = models.FloatField(null=True, blank=True)
    hemoglicoteste_HGT = models.IntegerField(null=True, blank=True)
    temperatura_TEMP = models.FloatField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)  
    altura = models.FloatField(null=True, blank=True) 
    data_triagem = models.DateField(auto_now_add=True, null=False)
    hora_triagem = models.TimeField(auto_now_add=True, null=True )
    
    #Campo a serem utilizado para filtrar os pacientes na triagem
    hora_envio_a_classificao = models.TimeField(null=True, blank=True)
    data_envio_a_classificao = models.DateField(null=True, blank=True)

    # Cotabilização de chamadas -------------------------------------
    respondeu_ao_chamado = models.BooleanField(default=False, null=True)
    chamadas_contabilizadas = models.IntegerField(default=0, null=True)
    medico_respondeu_ao_chamado = models.BooleanField(default=False, null=True)
    medico_chamadas_contabilizadas = models.IntegerField(default=0, null=True)
    # Fim Cotabilização de chamadas -------------------------------------

    classifica_tipo = models.ForeignKey(Classifica_risco_model, null=True, on_delete=models.PROTECT, verbose_name='Classificação de Emergência')
    observacao = RichTextField(null=True, blank=True)
    choices=(    
        ('', ''),    
        ('0', 'Não'),
        ('1','Sim'),
    )    
    preescrever_medicamento_medico = RichTextField(null=True, blank=True, default='Preescreva o medicamento para o paciente')
    # preescrever_medicamento_medico = models.TextField(max_length=500, null=True, default='Preescreva o medicamento para o paciente')
    encaminhamento = models.TextField(max_length=500, null=True, blank=True, default='Digite o encaminhamento do paciente')
    atestado = models.CharField(max_length=2, null=True,blank=True, default='0')
    exames = models.ManyToManyField(Exames_Model, null=True, blank=True)    
    # Atenção quem envia dados para o campo final_triagem é o medico, a triagem é finalizada com campo triagem_concluida no model envio_triagem
    final_triagem = models.CharField(max_length=3, null=True, default='')    
    final_triagem_time = models.DateField(auto_now=True, null=False)
    final_medico_atendimento = models.CharField(max_length=3, null=True, default='')
    nome_da_enfermeira = models.CharField(max_length=50, null=False, default='')    

    objects = TriagemManager()

    class Meta:
        ordering = ['classifica_tipo', 'hora_triagem', 'paciente_triagem__paciente_envio_triagem__idade']    

    def __str__ (self):
        return '{}'.format(self.paciente_triagem.paciente_envio_triagem.nome_social)
    
    def save(self, *args, **kwargs):
        # Verifica se o registro está sendo atualizado
        if self.pk is not None:
            # Verifica se há algum registro em Priority relacionado a este paciente_triagem
            if Priority.objects.filter(nome_priority=self.paciente_triagem.paciente_envio_triagem).exists():
                priority_classificacoes = ['Vermelho', 'Laranja', 'Amarelo']
                # Verifica se a classificação é diferente de 'Vermelho', 'Laranja' ou 'Amarelo'
                if self.classifica_tipo and self.classifica_tipo.classifica_tipo not in priority_classificacoes:
                    # Atualiza o campo classifica_tipo para 'Amarelo'
                    self.classifica_tipo = Classifica_risco_model.objects.get(classifica_tipo='Laranja')

        super().save(*args, **kwargs)
    
# Aplica ao paciente determinado tipo de atendimento   
choice = {
    ('Aguardando', 'Aguardando'),
    ('Em atendimento', 'Em atendimento'),
    ('Liberado', 'Liberado')
} 



class Atendimento_especializado(models.Model):
    tipo_atendimento = models.ForeignKey(Tipos_Atendimento, null=False, on_delete=models.CASCADE)
    situacao = models.CharField(choices=choice, max_length=30, null=True, default='Aguardando')
    descreve_solicitacao = models.TextField(max_length=300, null=True)
    nome_medico = models.CharField(max_length=30, null=False, default='Dr. Teste')
    pk_paciente = models.ForeignKey(triagem, null=False, on_delete=models.CASCADE)    


# xxxxxxxxxxxxxxxxxxxxxxxxxxxx CADASTRA E ALTERA USUARIOS xxxxxxxxxxxxxxxxxxxxxxxxxx
# Para criar outros campos para o usuario
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


#MODEL DO RAIO X -------------------------------------------------------
"""class RaioX_Model(models.Model):
    
    situacao = models.CharField"""