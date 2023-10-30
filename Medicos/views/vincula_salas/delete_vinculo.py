
from django.urls import  reverse_lazy
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  Salas_Atendimento
from django.views.generic import DeleteView


class DeleteProfissionaSala_Delet(LoginRequiredMixin, DeleteView):
    model = Salas_Atendimento
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context ['DeleteVinculo'] = 'DeleteVinculo'
        return context