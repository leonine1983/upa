from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import  UpdateView
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Triagem.models import Exames_Model
from Medicos.views.exames.exame_form import Exame_form_update
from django.core.paginator import Paginator


class Atualiza_Exame_UpdatView(LoginRequiredMixin, UpdateView):
    model = Exames_Model
    template_name = 'Medicos/exames/exames.html'
    form_class = Exame_form_update
    success_url = reverse_lazy('Medicos:cadastroExame')    
    success_message = "🏥 **Exame atualizado com sucesso!** 🎉"    
    paginate_by = 10 # Defina o número de itens por página


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["conteudo"] = "cadastraSala"
        # Obtenha todos os objetos da classe CadastroSala
        # e divida-os em páginas usando a classe Paginator
        paginator = Paginator(Exames_Model.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["object_list"] = paginator.get_page(page_number)
        context["update"] = "ok"
        return context
