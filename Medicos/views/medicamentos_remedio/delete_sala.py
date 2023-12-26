from django.urls import  reverse_lazy
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  CadastroSala


class Delete_Sala_Delet(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'    
    success_url = reverse_lazy('Medicos:cadastroSala')   
    success_message = "🏥 **Sala de Atendimento Médico Excluída com Sucesso!** 🎉"
    paginate_by = 5

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)            
            paginator = Paginator(CadastroSala.objects.all(), self.paginate_by)
            page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
          
            context["object_list"] = paginator.get_page(page_number)
            return context
