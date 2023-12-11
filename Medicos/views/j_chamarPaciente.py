from Atendimento.models import *
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Medico_atendimento
from django.shortcuts import get_object_or_404


def cadastrar_chamada(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome')
        nome = Medico_atendimento.objects.get(paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem__nome_social = nome_paciente).id

        # Certificar que o paciente existe no modelo Medico_atendimento

        print(f'nome enviado: {nome}')
        paciente = get_object_or_404(Medico_atendimento, paciente_medico_atendimento = nome)
        chamada = Chamar_P_para_atendimento(nome_paciente=paciente, request=request)
        chamada.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
    