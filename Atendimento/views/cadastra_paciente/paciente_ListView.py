
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from Atendimento.models import ficha_de_atendimento


class paciente_lista(LoginRequiredMixin, ListView):
    model = ficha_de_atendimento
    template_name = 'Atendimento/pacientes.html'
    paginate_by = 8

    #Fazer a pesquisa
    def get_queryset(self):
        txt_nome = self.request.GET.get('busca-paciente')

        if txt_nome:
            nome = ficha_de_atendimento.objects.filter(nome_social__icontains = txt_nome) | ficha_de_atendimento.objects.filter(cartao_sus__icontains = txt_nome) | ficha_de_atendimento.objects.filter(codigo_pacient__icontains = txt_nome)
        
        else:
            nome = ficha_de_atendimento.objects.all()

        return nome

    def form_valid(self, form):  
            form.instance.usuario = self.request.user

            url = super().form_valid(form)
            return url
    