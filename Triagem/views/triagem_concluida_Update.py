#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from Atendimento.models import envio_triagem

    
"""Confirma a finalização do pré-atendimento """
class triagem_concluida_Update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = envio_triagem
    fields = ['triagem_concluida']
    template_name = 'Triagem/triagem_confirm_final.html'
    success_url =reverse_lazy('Triagem:triagem-enfermaria')
    success_message = "Finalização do antendimento ao paciente feita com sucesso!"
    
        
    def get_success_url(self) -> str:
        return super().get_success_url()    
