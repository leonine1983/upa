#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import Cidade


class Cidade_CreateView(LoginRequiredMixin, CreateView):
    model = Cidade
    fields = ['cidade']
    template_name = 'Atendimento/cadastro_paciente.html'
    success_url = reverse_lazy('Atendimento:registro-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadas_rua'] = 'cidade'
        return context
