from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import  ListView
from Atendimento.models import *
from Medicos.models import  CadastroSala, Salas_Atendimento

class Lista_Salas_ListView(LoginRequiredMixin, ListView):

    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['profissionais'] = Salas_Atendimento.objects.all()
        return context

