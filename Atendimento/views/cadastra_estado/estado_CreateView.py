#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import Estado


class Estado_CreateView(LoginRequiredMixin, CreateView):
    model = Estado
    fields = ['estado']
    template_name = 'Atendimento/cadastro_paciente.html'
    success_url = reverse_lazy('Atendimento:registro-paciente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cadas_rua'] = 'estado'
        return context
