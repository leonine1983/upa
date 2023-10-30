from django.urls import  reverse_lazy
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  Salas_Atendimento
from django.views.generic import UpdateView


class VinculaProfissiona_sala_update(LoginRequiredMixin, UpdateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSalaUpdate'
        return context  

    