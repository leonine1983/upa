from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import  reverse_lazy
from django.core.paginator import Paginator
from django.views.generic import CreateView
from Medicos.models import CadastroSala
from Medicos.views.salas.salas_form import Salas_form

class Cadastra_Sala_view(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    form_class = Salas_form
    success_url = reverse_lazy('Medicos:cadastroSala')    
    success_message = "🏥 **Sala de Atendimento Médico Cadastrada com Sucesso!** 🎉"
    paginate_by = 10 # Defina o número de itens por página


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["conteudo"] = "cadastraSala"
        # Obtenha todos os objetos da classe CadastroSala
        # e divida-os em páginas usando a classe Paginator
        paginator = Paginator(CadastroSala.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["object_list"] = paginator.get_page(page_number)
        return context
