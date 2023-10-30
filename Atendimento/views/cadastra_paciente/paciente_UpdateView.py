from django.contrib.auth.decorators import login_required
#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from Atendimento.models import ficha_de_atendimento
from django.shortcuts import redirect


class paciente_atualizar(LoginRequiredMixin, UpdateView):
    model = ficha_de_atendimento
    fields = ['nome_social', 'data_nascimento','sexo', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado','CEP', 'nome_mae', 'responsavel', 'tel', 'cartao_sus'] 
    template_name = 'Atendimento/cadastro_paciente.html'    
    success_url = reverse_lazy("Atendimento:lista-paciente") 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['dados'] = 'update'
        return context

     #Se o usuario nao estiver logado
    login_url = reverse_lazy('Access_Login:access_login_page')
    redirect_field_name = 'next'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect (self.login_url + '?next=' + request.path)
        return super().dispatch(request, *args, **kwargs)