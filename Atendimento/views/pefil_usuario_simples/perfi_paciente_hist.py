from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from Medicos.models import Medico_atendimento
from Triagem.models import triagem
from Atendimento.models import envio_triagem, ficha_de_atendimento


"""Cria o histórico do paciente"""
@login_required
def perfil_paciente_hist(request, pk):    
    ficha_triagem = triagem.objects.all()
    ficha_medico_atendimento = Medico_atendimento.objects.all()

    ficha_paciente = ficha_de_atendimento.objects.filter(pk = pk)
    
    #Pega o id da ficha do paciente e filtra ele no model ENVIO_TRIAGEM
    ficha_envio_paciente = envio_triagem.objects.filter(paciente_envio_triagem_id = pk) 

    for f in ficha_envio_paciente:
        ficha_envio_id = f.id
        ficha_triagem = triagem.objects.filter(paciente_triagem_id = ficha_envio_id)

        for f in ficha_triagem:
            ficha_envio_triagem_id = f.id
            ficha_medico_atendimento = Medico_atendimento.objects.filter(paciente_medico_atendimento_id = ficha_envio_triagem_id)
    
    return render(request, 'Atendimento/perfil-paciente.html', {
        'db': ficha_paciente,
        'envio_triagem' : ficha_envio_paciente,
        'triagem' : ficha_triagem,
        'atendimento_medico' : ficha_medico_atendimento
    })
