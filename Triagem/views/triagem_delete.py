#Restringir acesso
from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from Triagem.models import triagem
from Triagem.forms import TriagemEnfermariaForm
from datetime import date
from django.db.models import Q



# Cadastra somente o id do paciente na TRIAGEM
class Triagem_Delete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = triagem
    template_name = 'Triagem/triagem.html'    
    success_message = "Paciente excluído da triagem com sucesso!"
    success_url = reverse_lazy('Triagem:triagem-enfermaria')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_titulo'] = "Excluir paciente da triagem"
        context['nome_objeto'] = self.get_object()
        return context
        
    