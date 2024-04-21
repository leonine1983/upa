from Medicos.models import Medico_atendimento
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils import timezone

def conclui_all(request):
    # Filtrando os objetos Medico_atendimento onde final_medico_atendimento é diferente de '1'
    atend = Medico_atendimento.objects.exclude(paciente_medico_atendimento__final_medico_atendimento='1')
    hoje = timezone.now().date()
    atend = atend.exclude( data_medico = hoje)

    # Verifica se há objetos encontrados
    if atend:
        # Itera sobre os objetos encontrados
        for at in atend:
            # Define o campo final_medico_atendimento como '1'
            at.paciente_medico_atendimento.final_medico_atendimento = '1'
            # Salva as alterações no objeto triagem
            at.paciente_medico_atendimento.save()
            messages.success(request, "Registros de atendimento ao paciente foram concluídos com êxito!")
    return redirect(reverse_lazy('Medicos:medico_prontuario'))
