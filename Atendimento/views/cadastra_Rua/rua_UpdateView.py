from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from Atendimento.models import Rua



class Rua_UpadateView(LoginRequiredMixin, UpdateView):
    model = Rua
    fields = ['rua_nome']
    template_name = 'Atendimento/cadastros_genericos/cadastros-genericos.html'
    success_url = reverse_lazy('Atendimento:list_bairro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_rua'] = 'bairro'
        return context
