from Triagem.models import triagem
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

def paciente_nao_atende (request, pk):
    # Verificar se o paciente existe
    paciente_triagem = get_object_or_404(triagem, pk = pk)

    # Informar que o paciente não respondeu ao chamado
    triagem.respondeu_ao_chamado = False

    # Indica a quantidade de chamados para o paciente
    triagem.chamadas_contabilizadas += 1

    # Salvo
    triagem.save()
    messages.info(request, "O paciente não respondeu ao chamado")

    return redirect(reverse("triagem:classifica"))
    