from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import   Salas_Atendimento


# Vicula Medico às SALAS -----------------------------------------------------------------------------
class VinculaProfissiona_sala_view(LoginRequiredMixin, CreateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSala'
        return context
