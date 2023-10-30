from django.urls import  reverse_lazy
from django.views.generic import DeleteView
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  CadastroSala


class Delete_Sala_Delet(LoginRequiredMixin, DeleteView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')
    context_object_name = 'nomeSala'
