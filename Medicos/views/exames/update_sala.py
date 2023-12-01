from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import  UpdateView
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  CadastroSala


class Atualiza_Sala_UpdatView(LoginRequiredMixin, UpdateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    fields = ['nome_Sala', 'descricao_Sala']
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        return context

