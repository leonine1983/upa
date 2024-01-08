#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import Etnia


class Etnia_CreateView(LoginRequiredMixin, CreateView):
    model = Etnia
    fields = ['etnia']
    template_name = 'Atendimento/cadastro_paciente.html'
    success_url = reverse_lazy('Atendimento:registro-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadas_rua'] = 'etnia'
        return context
