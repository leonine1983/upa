from Triagem.models import triagem
from Medicos.models import Chamar_P_para_atendimento
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

def paciente_nao_atende (request, pk):
     # Verificar se o paciente existe
    paciente_triagem = get_object_or_404(triagem, pk=pk)

    # Informar que o paciente não respondeu ao chamado
    paciente_triagem.respondeu_ao_chamado = True

    # Indica a quantidade de chamadas para o paciente
    paciente_triagem.chamadas_contabilizadas += 1

    # Salvar
    paciente_triagem.save()
    messages.info(request, "O paciente não respondeu ao chamado")

    # Exclui os registros de chamado do paciente ativo
    Chamar_P_para_atendimento.objects.filter(nome_paciente=paciente_triagem).delete()

    return redirect(reverse("Triagem:triagem-enfermaria"))

    