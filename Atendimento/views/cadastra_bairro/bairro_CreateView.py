#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import Bairro


class Bairro_CreateView(LoginRequiredMixin, CreateView):
    model = Bairro
    fields = ['bairro_nome']
    template_name = 'Atendimento/cadastros_genericos/cadastros-genericos.html'
    success_url = reverse_lazy('Atendimento:list_bairro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadas_bairro'] = 'bairro'
        return context