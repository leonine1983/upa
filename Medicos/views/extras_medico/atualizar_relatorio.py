from Medicos.models import Medico_atendimento
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def atualizar_relatorio(request, pk):
    medico_atendimento = get_object_or_404(Medico_atendimento, pk = pk)
    medico_atendimento.relatorio_impresso = True
    medico_atendimento.save()
    return JsonResponse({'success':True})