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
    triagem_filtro = triagem.objects.exclude(final_medico_atendimento = 1)
    return render(request, 'Medicos/medico.html', {
        'n_pacientes_triagem': len(triagem_filtro),
        'object_list' : triagem_filtro,
        'atendimento_especi': Atendimento_especializado.objects.all(),
        'atendimentos_hoje': Medico_atendimento.objects.filter(data_medico = datetime.now())
    })
    