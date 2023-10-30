from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.urls import  reverse_lazy
#restrição de acesso
from django.views.generic import UpdateView
from Atendimento.models import *
from Medicos.models import CustomUser


class MedicoUpdateView_extra(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['telefone', 'data_nascimento', 'endereco', 'crm']
    template_name = 'Medicos/criar_medicos/update.html'
    success_url = reverse_lazy('Medicos:medico_signup')

    def get_context_data(self, **kwargs):
        medicos_group = Group.objects.get(name='group_Medicos')
        users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'user__id', 'id','user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )

        context = super().get_context_data(**kwargs)
        context["user_update"] =CustomUser.objects.filter(pk = self.kwargs['pk'])
        context["users"] = users
        context["custom"] = 'custom'
        return context 
