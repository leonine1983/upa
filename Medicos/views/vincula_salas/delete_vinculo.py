
from django.urls import  reverse_lazy
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  Salas_Atendimento
from django.views.generic import DeleteView
from django.core.paginator import Paginator


class DeleteProfissionaSala_Delet(LoginRequiredMixin, DeleteView):
    model = Salas_Atendimento
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salasProfissionalCreate')
    paginate_by = 5
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['DeleteVinculo'] = 'DeleteVinculo'        
        paginator = Paginator(Salas_Atendimento.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["vinculo_sala"] = 'ok'
        context["object_list"] = paginator.get_page(page_number)
        return context
