from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import  ficha_de_atendimento
from django.views.generic.list import ListView

class ListagemPessoaBairroCidade(LoginRequiredMixin, ListView):
    model = ficha_de_atendimento
    template_name = 'Atendimento/outras_listagens/listaPessoasBairro.html'

    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['pessoas'] = ficha_de_atendimento.objects.filter(cidade__cidade = "Vera Cruz")

       return context
   
