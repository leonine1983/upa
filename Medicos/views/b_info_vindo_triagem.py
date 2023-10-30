from django.contrib.auth.decorators import login_required
from Atendimento.models import *
from Triagem.models import triagem
from django.shortcuts import  render

@login_required
def medico_atendimento_view(request, pk):
    dados_triagem = triagem.objects.filter(pk=pk)
    for dados in dados_triagem:
        #tempo1 =datetime(dados.hora_triagem)
        dados = dados.paciente_triagem_id        
        dados_triagem = envio_triagem.objects.filter(pk=dados) 
        info_Hora_Tri = triagem.objects.filter(paciente_triagem_id=dados)
        for t in info_Hora_Tri:
            info_Hora_envioT = t.hora_triagem     

    dados_envio_triagem = envio_triagem.objects.filter(pk=dados)
    for dados in dados_envio_triagem:
        #tempo2 =time(dados.horario_triagem)
        dados = dados.paciente_envio_triagem_id 
        info_Hora_envioT = envio_triagem.objects.filter(paciente_envio_triagem_id = dados)
        for t in info_Hora_envioT:
            info_Hora_envioT = t.horario_triagem

    #contem o horário da triagem
    info_Hora_envioT

    #contem o horário do envio_triagem
    info_Hora_envioT   
        
    return render(request, 'Medicos/medico_atendimento.html', {
        'paciente_triagem' : triagem.objects.filter(pk=pk), 
        'ficha_atendimento' : ficha_de_atendimento.objects.filter(pk=dados),
        'dados_triagem' : dados_triagem,
        #'tempo' : tempo         
    } )
