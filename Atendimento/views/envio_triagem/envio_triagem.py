from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem 

class envio_paciente_a_triagem(LoginRequiredMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')