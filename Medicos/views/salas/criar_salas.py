from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from Atendimento.models import *
from Medicos.models import  CadastroSala


class Cadastra_Sala_view(LoginRequiredMixin, CreateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    fields = ['nome_Sala', 'descricao_Sala']
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conteudo"] = "cadastraSala"
        return context
