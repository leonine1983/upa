from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

from Atendimento.models import Rua



class Rua_ListView(LoginRequiredMixin, ListView):
    model = Rua
    template_name = 'Atendimento/cadastros_genericos/cadastros-genericos.html'
    context_object_name = 'listView'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update_rua'] = 'bairro'
        return context