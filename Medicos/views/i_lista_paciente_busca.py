from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Atendimento.models import *


# lista de paciente e pesquisa com dados do historico
class paciente_lista_historico(LoginRequiredMixin, ListView):
    model = ficha_de_atendimento
    template_name = 'Medicos/perfis/pacientes.html'
    paginate_by = 10
    
    # Fazer a pesquisa
    def get_queryset(self):
        txt_nome = self.request.GET.get('busca-paciente')

        if txt_nome:
            nome = ficha_de_atendimento.objects.filter(nome_social__icontains = txt_nome) | ficha_de_atendimento.objects.filter(cartao_sus__icontains = txt_nome)
    
        else:
            nome = ficha_de_atendimento.objects.all()

        return nome

    def form_valid(self, form):  
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url
