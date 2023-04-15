
from datetime import date, datetime, timedelta

from django.contrib.auth.decorators import login_required
#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from Medicos.models import Medico_atendimento
from Triagem.models import triagem
from django.db.models import Count

from .models import envio_triagem, ficha_de_atendimento
from Medicos.models import Chamar_P_para_atendimento
from configUPA.models import config_Marquee, Video_Backgroud_Painel

#restringir por 



# Create your views here.
@login_required
def pagina_inicial(request):
    data = datetime.today() 
    paciente_dia = envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data)  
    pacient_localidade = paciente_dia.values('paciente_envio_triagem__bairro').annotate(Total = Count('paciente_envio_triagem__bairro') )
    
   
    return render(request, 'Atendimento/pagina_inicial.html', {
        'quant' : int(len(ficha_de_atendimento.objects.all())),
        'quant_homem' : len(ficha_de_atendimento.objects.filter(sexo = 1)),
        'quant_mulher' : len(ficha_de_atendimento.objects.filter(sexo = 2)),
        'nome_sistema' : "GePA - Gestão de Pronto Atendimento",
        'nome_estabelecimento': 'UPA',
        'quant_atendimentos_diario': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data)),
        
        'quant_atendimentos_diario_H': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1)),         
        'quant_H_idosos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=60, paciente_envio_triagem__idade__lte=130)),
        'quant_H_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=18, paciente_envio_triagem__idade__lte=59.99)), 
        'quant_H_adolescentes': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=12, paciente_envio_triagem__idade__lte=17.9)), 
        'quant_H_criancas': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=1, paciente_envio_triagem__idade__lte=11.9)), 
        'quant_H_bebe': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__idade=0)), 
        #'quant_H_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 1) ),
        'quant_atendimentos_diario_F': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 2)),        
        'quant_F_idosos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 2) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=60, paciente_envio_triagem__idade__lte=130)),
        'quant_F_adultos': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 2) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=18, paciente_envio_triagem__idade__lte=59.99)), 
        'quant_F_criancas': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 2) & envio_triagem.objects.filter(paciente_envio_triagem__idade__gte=1, paciente_envio_triagem__idade__lte=12)), 
        'quant_F_bebe': len(envio_triagem.objects.filter(triagem_concluida = 1) & envio_triagem.objects.filter(data_triagem_concluida = data) & envio_triagem.objects.filter(paciente_envio_triagem__sexo = 2) & envio_triagem.objects.filter(paciente_envio_triagem__idade=0)), 
      
        'qquant_localidades': envio_triagem.objects.values('paciente_envio_triagem__bairro').annotate(total=Count('paciente_envio_triagem__bairro')),
        'quant_localidades': pacient_localidade    
        
    })


class paciente_cadastro(LoginRequiredMixin, CreateView):
    model = ficha_de_atendimento
    fields = ['nome_social', 'data_nascimento','sexo', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado','CEP', 'nome_mae', 'responsavel', 'tel', 'cartao_sus'] 
    template_name = 'Atendimento/cadastro_paciente.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        url = reverse_lazy('Atendimento:envio_paciente_a_triagem_2', args=[self.object.pk])
        print('ID do objeto criado:', self.object.pk)
        return url


class paciente_atualizar(UpdateView):
    model = ficha_de_atendimento
    fields = ['nome_social', 'data_nascimento','sexo', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado','CEP', 'nome_mae', 'responsavel', 'tel', 'cartao_sus'] 
    template_name = 'Atendimento/cadastro_paciente.html'    
    success_url = reverse_lazy("Atendimento:lista-paciente") 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['dados'] = 'update'
        return context



class paciente_lista(LoginRequiredMixin, ListView):
    model = ficha_de_atendimento
    template_name = 'Atendimento/pacientes.html'
    paginate_by = 8

    #Fazer a pesquisa
    def get_queryset(self):
        txt_nome = self.request.GET.get('busca-paciente')

        if txt_nome:
            nome = ficha_de_atendimento.objects.filter(nome_social__icontains = txt_nome) | ficha_de_atendimento.objects.filter(cartao_sus__icontains = txt_nome)
        
        else:
            nome = ficha_de_atendimento.objects.all()

        return nome

    def form_valid(self, form):  
            form.instance.usuario = self.request.user

            url = super().form_valid(form)
            return url

"""Cria o perfil basico do paciente"""
@login_required
def perfil_paciente(request, pk):    
    ficha_paciente = ficha_de_atendimento.objects.filter(pk = pk)   

    return render(request, 'Atendimento/perfil-paciente.html', {
        'db': ficha_paciente, 
    })


"""Cria o histórico do paciente"""
@login_required
def perfil_paciente_hist(request, pk):    
    ficha_triagem = triagem.objects.all()
    ficha_medico_atendimento = Medico_atendimento.objects.all()

    ficha_paciente = ficha_de_atendimento.objects.filter(pk = pk)
    
    #Pega o id da ficha do paciente e filtra ele no model ENVIO_TRIAGEM
    ficha_envio_paciente = envio_triagem.objects.filter(paciente_envio_triagem_id = pk) 

    for f in ficha_envio_paciente:
        ficha_envio_id = f.id
        ficha_triagem = triagem.objects.filter(paciente_triagem_id = ficha_envio_id)

        for f in ficha_triagem:
            ficha_envio_triagem_id = f.id
            ficha_medico_atendimento = Medico_atendimento.objects.filter(paciente_medico_atendimento_id = ficha_envio_triagem_id)

    #Encontrado o ID das fichas de atendimento desse paciente, filtramos o model triagem para saber os 
    #IDs de pre-atendimento desse paciente
    
    

    #Encontrado o ID das fichas de triagem desse paciente, filtramos o model Medico_atendimento para saber os 
    #IDs de atendimento médico desse paciente
    
    
    return render(request, 'Atendimento/perfil-paciente.html', {
        'db': ficha_paciente,
        'envio_triagem' : ficha_envio_paciente,
        'triagem' : ficha_triagem,
        'atendimento_medico' : ficha_medico_atendimento
    })



@login_required
def perfil_paciente_medico(request, pk):
    masculino = 'Masculino'
    #Pega o Id do Atendimento médico
    atend_med = Medico_atendimento.objects.filter(pk = pk)
    for at in atend_med:
        atend_tri = at.paciente_medico_atendimento_id

    atend_tri = triagem.objects.filter(pk = atend_tri)
    for at in atend_tri:
        atend_env = at.paciente_triagem_id

    atend_env = envio_triagem.objects.filter(pk = atend_env)
    for at in atend_env:
        ficha_atend = at.paciente_envio_triagem_id

    ficha_atend = ficha_de_atendimento.objects.filter(pk = ficha_atend)

    

    
    return render(request, 'Atendimento/perfil-paciente.html', {
        'atend_med': atend_med,
        'atend_tri': atend_tri,
        'atend_env': atend_env,
        'masculino': masculino,
        'valor' :envio_triagem.objects.filter(pk = pk)    
    })
   
 



#------------------------------------------------------------------------
#FILA DE TRIAGEM
#------------------------------------------------------------------------

#criar a pagina de cadastro
class envio_paciente_a_triagem(LoginRequiredMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')


#criar a pagina de cadastro
class envio_paciente_a_triagem_2(LoginRequiredMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']  

    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context ['get_id'] = ficha_de_atendimento.objects.filter(id = self.kwargs['pk']) 
        return context
    
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')

#deleta
class delete_paciente_a_triagem(LoginRequiredMixin, DeleteView):
    model = envio_triagem
    template_name = 'Atendimento/delete_fila_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')


#cria a lista
@login_required
def lista_de_paciente_na_triagem(request):
    
    start_date = request.GET.get('start_date')
    date_today = datetime.today()
    #converte o formato da data
    date_hoje = '{}-{}-{}'.format(date_today.year, date_today.month, date_today.day)
    
    if start_date:
        #converte a str objects em date
        date = datetime.strptime(start_date, '%Y-%m-%d')        
        
        #converte o formato da data
        date_format = '{}-{}-{}'.format(date.year, date.month, date.day)

        object_list = envio_triagem.objects.all()
       
        #formata o mês por extenso
        #mes_extenso = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}    
        #mes = mes_extenso[date.month]
        #data = f"{date.day} de {mes} de {date.year}"
        #object_list = envio_triagem.objects.all()
        print(date_format)      
        

        
        if date_format:
            object_list = envio_triagem.objects.filter(data_envio_triagem = date_format) & envio_triagem.objects.exclude(triagem_concluida = 1)
        else:             
            object_list = envio_triagem.objects.all() & envio_triagem.objects.exclude(triagem_concluida = 1)
    else:
        object_list = envio_triagem.objects.filter(data_envio_triagem = date_hoje) & envio_triagem.objects.exclude(triagem_concluida = 1)
        #object_list = envio_triagem.objects.all()
        #print(f'a data de hoje e {date_hoje}')

    data_hoje = datetime.today() 
   

    return render(request, 'Atendimento/envio_a_triagem.html', {
        'lista_db' : object_list,
        'data_hoje' : date_hoje,
        'url' :   'Atendimento:envio_paciente_a_triagem',  
    })



#cria o painel para chamar os pacientes
import io
from django.shortcuts import render
from gtts import gTTS

import base64
from gtts import gTTS

import io
from django.shortcuts import render
from gtts import gTTS
import base64

from django.shortcuts import render
from gtts import gTTS
import base64
import io

from Medicos.models import Chamar_P_para_atendimento

import json
from channels.layers import get_channel_layer



# Importações necessárias
from django.http import JsonResponse
from django.shortcuts import render
from Medicos.models import Chamar_P_para_atendimento
from gtts import gTTS
import io
import base64
from datetime import datetime
from configUPA.models import config_Marquee


# View para gerar o áudio e renderizar o template com o áudio em base64
def painel(request):    
    # Enviar o áudio como contexto para o template
    configUpa = config_Marquee.objects.all()
    video = Video_Backgroud_Painel.objects.first().video_file
    print (f'esse é o video {video}')
    return render(request, 'Atendimento/painel_pacientes/painel.html', {
        'now': datetime.now(),
        'configUpa': configUpa,
        'videoUpa': video})






from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Salas_Atendimento, CadastroSala


def chamar_paciente(request):    
    
    # Busca o id do profissional de saúde na primeira chamada de atendimento
    nome_paciente = Chamar_P_para_atendimento.objects.first().nome_paciente
    nome_paciente_2 = Chamar_P_para_atendimento.objects.first().nome_paciente
    profissional_id = Chamar_P_para_atendimento.objects.first().profissionalSaude_id_id   
    print(f'id do profissional {profissional_id}')     
    # Busca o objeto Salas_Atendimento que corresponde ao profissional de saúde encontrado
    sala_do_usuario = Salas_Atendimento.objects.get(profissionalSaude_id=profissional_id)
    print(f'id da sala: {sala_do_usuario}')
    # Busca o nome da sala correspondente no modelo CadastroSala
    nome_sala = CadastroSala.objects.get(id=sala_do_usuario.nomeSala_id).nome_Sala        
    print(f'nome da sala {nome_sala}')

    nome_paciente = f'Paciente {nome_paciente}  por favor se dirigir à sala de {nome_sala}'
    print(f'essa e a data {Chamar_P_para_atendimento.objects.first().data_chamada}')
       
   

    # Gerar o áudio em memória
    tts = gTTS(text=nome_paciente, lang='pt-br')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    # Ler os dados do áudio em memória e codificá-los em base64
    audio_content = audio_file.read()
    audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    # Montar a resposta JSON
    response_data = {
        'nome_paciente': nome_paciente,
        'nome_sala': nome_sala,
        'data_chamada': Chamar_P_para_atendimento.objects.first().data_chamada,
        'nome_paciente2': nome_paciente_2,
        'data_criacao': Chamar_P_para_atendimento.objects.first().data_criacao,
        'data_atualizacao': Chamar_P_para_atendimento.objects.first().data_atualizacao,
        'audio_base64': audio_base64,    
    }
    return JsonResponse(response_data)





from django.http import JsonResponse
from Triagem.models import ChamarPaciente

def chamar_paciente_triagem(request):
    nome_paciente_triagem = f'Paciente {ChamarPaciente.objects.first().nome_paciente} por favor se dirigir à sala de Atendimento Médico'
    nome_paciente_triagem2 = ChamarPaciente.objects.first().nome_paciente
    
    print(f"testando como esta as coisa: {nome_paciente_triagem}")

    # Gerar o áudio em memória
    tts = gTTS(text=nome_paciente_triagem, lang='pt-br')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    # Ler os dados do áudio em memória e codificá-los em base64
    audio_content = audio_file.read()
    audio_base64 = base64.b64encode(audio_content).decode('utf-8')
    print('audio_base64:', audio_base64)  # Adicionado para depurar o problema

    # Montar a resposta JSON
    response_data = {
        'nome_paciente': nome_paciente_triagem,
        'nome_paciente2': nome_paciente_triagem2,
        'data_criacao': ChamarPaciente.objects.first().data_criacao,
        'audio_base64': audio_base64,
    }

    
    return JsonResponse(response_data)
