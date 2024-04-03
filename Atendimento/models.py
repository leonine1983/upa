from datetime import date,timedelta, datetime
from django.db.models import Case, When, Value, BooleanField
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver


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

choices=(      
        ('0', 'Não'),
        ('1','Sim'),
    )
class ficha_de_atendimento(models.Model):
    nome_social = models.CharField(max_length=40, null=False, default='', verbose_name="Nome Social (Como a pessoa que ser chamada no painel)")
    nome_completo = models.CharField(max_length=50, null=True, default='', verbose_name="Nome completo (Como está escrito no RG)")
    codigo_pacient = models.CharField(max_length=8, null=True, verbose_name="Código do paciente")
    idade = models.IntegerField(null=False, default='00')    
    etnia = models.ForeignKey(Etnia, null=True, on_delete=models.CASCADE)
    data_nascimento = models.DateField( auto_now=False, auto_now_add=False, null=True, default='')
    sexo = models.ForeignKey(genero_sexual, null=True, on_delete=models.CASCADE)
    RG = models.CharField(max_length=13, null=True, default='')
    CPF = models.CharField(max_length=14, null=True, default='')
    nacionalidade = models.CharField(max_length=30, null=True, default='')
    rua = models.CharField(max_length=40, null=True, default='')
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE, related_name='fichas_atendimento_bairro')
    cidade = models.ForeignKey(Cidade, null=True, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, null=True, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, related_name='fichas_atendimento_pais')
    CEP = models.CharField(max_length=9, null=True, default='')
    nome_mae = models.CharField(max_length=40, null=True, default='')
    responsavel = models.CharField(max_length=30, null=True)
    tel = models.CharField(max_length=16, null=True, default='')
    data_cadastro = models.DateField(auto_now_add=True, null=False)
    data_update = models.DateField(auto_now=True, null=True)
    horario_cadastro = models.TimeField(null=True, auto_now_add=True)
    cartao_sus = models.CharField(max_length=15, null=True)
    ultimo_pk = None
    alergias = models.CharField(max_length=3, default='0', choices= choices, )
    conteudo_alergia = models.TextField(max_length=500, null=True, blank=True, default='Não possui alergias (Para tornar editável essa área, é necessário informar que o paciente possui alergias)')
    comorbidades = models.CharField(max_length=3, default='0', choices= choices )
    conteudo_comorbidades = models.TextField(max_length=500, null=True, blank=True, default='Não possui comobirdades (Para tornar editável essa área, é necessário informar que o paciente possui comobirdades)')
    nome_recepcionista = models.CharField(max_length=40, null=True, default='')
    
    class Meta:
        ordering = ['nome_social']          
    
    def save(self, *args, **kwargs):
        
        today = date.today()
        self.idade = today.year - self.data_nascimento.year - ((today.month, today.day) < (self.data_nascimento.month, self.data_nascimento.day))
        super().save(*args, **kwargs)
        return self.pk
        
    def __str__ (self):
        return f'Codigo: {self.codigo_pacient} | Nome Social: {self.nome_social} | Idade: {self.RG} anos | Idade: {self.idade} anos {"| ⚠️ Paciente Alergico " if not self.alergias else ""}'
    
    from datetime import datetime
    @receiver(post_migrate)
    def crie_registro(sender, **kwargs):
        paciente = ficha_de_atendimento.objects.filter(nome_social = "Enzzo Cauan Lins da Silva")
        paciente2 = ficha_de_atendimento.objects.filter(nome_social = "Bruna Cauanne Lins da Silva")
        paciente3 = ficha_de_atendimento.objects.filter(nome_social = "Cintia Teixeira Lins")
        paciente4 = ficha_de_atendimento.objects.filter(nome_social = "Vanda Paulino Cerqueira")
        paciente5 = ficha_de_atendimento.objects.filter(nome_social = "Rogério Cerqueira da Silva")
        paciente6 = ficha_de_atendimento.objects.filter(nome_social = "Rogerio Cerqueira da Silva")
        if not paciente:
            data_nasci = datetime.strptime('04/02/2013', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = 'Enzzo Cauan Lins da Silva',
                nome_completo = 'Enzzo Cauan Lins da Silva',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Cintia Teixeira Lins',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
        if not paciente2:
            data_nasci = datetime.strptime('22/05/2005', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = 'Bruna Cauanne Lins da Silva',
                nome_completo = 'Bruna Cauanne Lins da Silva',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Cintia Teixeira Lins',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
        if not paciente3:
            data_nasci = datetime.strptime('26/10/1988', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = "Cintia Teixeira Lins",
                nome_completo = 'Cintia Teixeira Lins',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Cintia Teixeira Lins',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
        if not paciente4:
            data_nasci = datetime.strptime('26/10/1965', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = "Vanda Paulino Cerqueira",
                nome_completo = 'Vanda Paulino Cerqueira',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Alaíde',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
        if not paciente5:
            data_nasci = datetime.strptime('05/08/1983', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = "Rogério Cerqueira da Silva",
                nome_completo = 'Rogério Cerqueira da Silva',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Vanda Paulino Cerqueira',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
        if not paciente6:
            data_nasci = datetime.strptime('05/08/1983', "%d/%m/%Y")
            ficha_de_atendimento.objects.create(
                nome_social = "Rogerio Cerqueira da Silva",
                nome_completo = 'Rogério Cerqueira da Silva',
                nome_recepcionista = 'Dariuma',
                nome_mae = 'Vanda Paulino Cerqueira',
                data_nascimento = data_nasci,
                bairro = Bairro.objects.get(id=9),
                pais = Pais.objects.get(id=1)
            )
    
    
    
class Priority (models.Model):
    nome_priority = models.ForeignKey(ficha_de_atendimento, related_name = "rel_priority", null= True, on_delete = models.CASCADE)

    @receiver(post_migrate)
    def criar_registro(sender, **kwargs):
        if not Priority.objects.exists():
            Priority.objects.create(
                nome_priority = ficha_de_atendimento.objects.get(nome_social = 'Enzzo Cauan Lins da Silva')
            )
            Priority.objects.create(
                nome_priority = ficha_de_atendimento.objects.get(nome_social = 'Bruna Cauanne Lins da Silva')
            )
            Priority.objects.create(
                nome_priority = ficha_de_atendimento.objects.get(nome_social = 'Cintia Teixeira Lins')
            )
            Priority.objects.create(
                nome_priority = ficha_de_atendimento.objects.get(nome_social = 'Vanda Paulino Cerqueira')
            )

    def __str__(self):
        return self.nome_priority.nome_social
    

class EnvioTriagemManager(models.Manager):
    def get_queryset(self):
        # Recuperar os pacientes na lista de prioridades
        priority_patients = Priority.objects.values_list('nome_priority__id', flat=True)

        # Anotar o queryset de envio_triagem com um campo indicando se o paciente está na lista de prioridades ou não
        queryset = super().get_queryset().annotate(
            is_priority=Case(
                When(paciente_envio_triagem__id__in=priority_patients, then=Value(True)),
                default=Value(False),
                output_field=BooleanField()
            )
        ).order_by('-is_priority', 'horario_triagem')
        
        return queryset

class envio_triagem(models.Model):
    paciente_envio_triagem = models.ForeignKey(ficha_de_atendimento, related_name='rel_ficha_atendimento', null=False, on_delete=models.PROTECT)       
    cod_triagem = models.CharField(max_length=50, null=True) 
    nome_acompanhante = models.CharField(max_length=50, null=True, default='Ele mesmo')  
    data_envio_triagem = models.DateField(auto_now_add=True, null=True)
    horario_triagem = models.TimeField(auto_now_add=True, null=True)
    triagem_concluida = models.CharField(max_length=1, null=True)
    data_triagem_concluida = models.DateField(auto_now=True, null=True)
    retornou_em_menos_de_48_horas =  models.BooleanField(default=False, null=False)
    horas48 =  models.BooleanField(default=False, null=False)
    prioridade = models.CharField(max_length=3, default='0', choices= choices )
    nome_recepcionista = models.CharField(max_length=40, null=True, default='')

    objects = EnvioTriagemManager()
 
    class Meta:
        ordering = ['horario_triagem']
        permissions = [('Acesso_permitido_envio_Tri', 'Acesso permitido para envio à Fila de Triagem')]

    def __str__ (self):
        return f'Codigo: {self.paciente_envio_triagem.codigo_pacient} | Nome: {self.paciente_envio_triagem.nome_social} | Idade: {self.paciente_envio_triagem.idade} anos {"<<< PRIORIDADE >>>" if self.prioridade == "1"  else ""}'
    

class Licenca(models.Model):
    expiracao = models.DateTimeField()
    ativa = models.BooleanField(default=True)

    def __str__(self):
        status = "Ativa" if self.ativa else "Inativa"
        data_formatada = self.expiracao.strftime("%d de %B de %Y")
        return f"Licença (Expiração: {data_formatada}, Status: {status})"    
    
    @receiver(post_migrate)
    def create_registros(sender, **kwargs):
        if not Licenca.objects.exists():
            # Obtenha a data atual com informações de fuso horário
            expiracao = datetime.now() + timedelta(days=20)
            
            # Crie a instância de Licenca
            Licenca.objects.create(
                expiracao=expiracao,
                ativa=True
            )
