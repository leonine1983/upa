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
    triagem_filtro = triagem.objects.exclude(final_medico_atendimento=1)
    nao_finalizado = []
    triage_all = triagem.objects.all()

    for ated_espec in triage_all:
        try:
            nao_finalizado.append(ated_espec.medico_atendimento.paciente_medico_atendimento.final_medico_atendimento)
        except Medico_atendimento.DoesNotExist:
            pass

    return render(request, 'Medicos/medico.html', {
        'object_list': triagem_filtro,
        'atendimento_especi': Atendimento_especializado.objects.all(),
        'atendimentos_hoje': Medico_atendimento.objects.filter(data_medico=datetime.now()),
        'atend_aguarda_final': triagem_filtro,
        'nao_finalizado': nao_finalizado
    })
    