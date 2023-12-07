from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from django.core.paginator import Paginator
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import   Salas_Atendimento, CadastroSala


# Vicula Medico às SALAS -----------------------------------------------------------------------------
class VinculaProfissiona_sala_view(LoginRequiredMixin, CreateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salasProfissionalCreate')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSala'
        paginator = Paginator(Salas_Atendimento.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["vinculo_sala"] = 'ok'
        context['object_list'] = paginator.get_page(page_number)
        return context
    
