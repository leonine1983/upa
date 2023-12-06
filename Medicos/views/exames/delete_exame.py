from django.urls import  reverse_lazy
from django.views.generic import DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  CadastroSala
from Triagem.models import Exames_Model
from Medicos.views.exames.exame_form import Exame_form


class Delete_Exame_Delet(LoginRequiredMixin,SuccessMessageMixin, DeleteView):
    model = Exames_Model
    template_name = 'Medicos/exames/exames.html'
    success_url = reverse_lazy('Medicos:cadastroExame')    
    success_message = "🏥 **Exame deletado com sucesso!** 🎉"
    paginate_by = 10 # Defina o número de itens por página

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)            
            paginator = Paginator(Exames_Model.objects.all(), self.paginate_by)
            page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
          
            context["object_list"] = paginator.get_page(page_number)
            context["delete"] = 'ok'
            return context
