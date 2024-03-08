from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Atendimento.models import *
from Triagem.models import triagem
from django.contrib.auth.hashers import make_password
from Triagem.models import Atendimento_especializado
from Medicos.models import Medico_atendimento
from datetime import datetime


# Essa View, retorna a lista de pacientes que passaram pela Triagem e aguardam atendimento médico.
@login_required
def medico_protuario_view_(request):
    busca_paciente = request.GET.get('busca_paciente')
    nao_finalizado = []
    if busca_paciente:
        triagem_filtro = triagem.objects.exclude(final_medico_atendimento=1) and triagem.objects.filter(paciente_triagem__paciente_envio_triagem__nome_social__icontains = busca_paciente)    
        checked = 'checked'
        """
                   ficha_de_atendimento.objects.filter(cartao_sus__icontains=txt_nome) | \
                   ficha_de_atendimento.objects.filter(codigo_pacient__icontains=txt_nome) | \
                   ficha_de_atendimento.objects.filter(CPF__icontains=txt_nome) | \
                   ficha_de_atendimento.objects.filter(RG__icontains=txt_nome) 
        
        
        """
    else:
        triagem_filtro = triagem.objects.exclude(final_medico_atendimento=1)
        checked = ''
    triage_all = triagem.objects.all()

    

    for ated_espec in triage_all:
        
        try:
            nao_finalizado.append(ated_espec.medico_atendimento.paciente_medico_atendimento.final_medico_atendimento)
            
        except Medico_atendimento.DoesNotExist:
            pass
    print(f'esse e o resultado da pesqisa: {nao_finalizado}')

    
    return render(request, 'Medicos/medico.html', {
        'object_list': triagem.objects.exclude(final_medico_atendimento=1),
        'atendimento_especi': Atendimento_especializado.objects.all(),
        'atendimentos_hoje': Medico_atendimento.objects.filter(data_medico=datetime.now()),
        'atend_aguarda_final': triagem_filtro,
        'checked5' : checked,
        'nao_finalizado': nao_finalizado,
        
    })
    