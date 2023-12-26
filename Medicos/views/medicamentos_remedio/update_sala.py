from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import  UpdateView
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import  CadastroSala
from django.core.paginator import Paginator


class Atualiza_Sala_UpdatView(LoginRequiredMixin, UpdateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    fields = ['nome_Sala', 'descricao_Sala']
    success_url = reverse_lazy('Medicos:salas')
    paginate_by = 10 # Defina o número de itens por página

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        return context
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        # Obtenha todos os objetos da classe CadastroSala
        # e divida-os em páginas usando a classe Paginator
        paginator = Paginator(CadastroSala.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["object_list"] = paginator.get_page(page_number)
        return context

