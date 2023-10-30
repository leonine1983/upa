#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.auth.models import Group
#from .forms import MedicoSignUpForm
from Medicos.models import CustomUser 
from .MedicoSignUpForm import *


class DeleteUserDelet(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'Triagem/cria_enfEtec/cria_enfEtec _delete.html' 
    success_message = 'Usuário excluído com sucesso.'
    success_url = reverse_lazy('Triagem:user_create')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medicos_group = Group.objects.get(name='group_Medicos')
        group_UPA_Admin = Group.objects.get(name='group_UPA-Admin')
        users = CustomUser.objects.exclude(user__groups=medicos_group).exclude(user__groups=group_UPA_Admin).select_related('user').values(
        'id', 'user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )        
        context['users'] = users
        pk = self.kwargs['pk']

        context['up'] = f'{CustomUser.objects.get(pk=pk).user.first_name} {CustomUser.objects.get(pk=pk).user.last_name}'
        return context
