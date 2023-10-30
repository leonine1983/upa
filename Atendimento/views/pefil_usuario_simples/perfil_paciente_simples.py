from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Atendimento.models import ficha_de_atendimento


"""Cria o perfil basico do paciente"""
@login_required
def perfil_paciente(request, pk):    
    ficha_paciente = ficha_de_atendimento.objects.filter(pk = pk)   

    return render(request, 'Atendimento/perfil-paciente.html', {
        'db': ficha_paciente, 
    })