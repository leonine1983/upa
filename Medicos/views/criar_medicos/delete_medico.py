from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import DeleteView
from Atendimento.models import *
from Medicos.models import CustomUser, User

# views.py
from django.contrib.auth.hashers import make_password


class MedicoDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'Medicos/criar_medicos/update.html'
    success_url = reverse_lazy('Medicos:medico_signup')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paciente_nome'] =User.objects.get(pk=self.kwargs['pk']).first_name
        context['conteudo_view'] = 'medico_delete'
        medicos_group = Group.objects.get(name='group_Medicos')
        context['users'] = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'id','user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )
        return context