from Atendimento.models import *
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento


def cadastrar_chamada(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome')
        chamada = Chamar_P_para_atendimento(nome_paciente=nome_paciente, request=request)
        chamada.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    