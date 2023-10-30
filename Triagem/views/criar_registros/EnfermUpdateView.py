from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView
from django.contrib.auth.models import Group
#from .forms import MedicoSignUpForm
from Medicos.models import CustomUser
from .MedicoSignUpForm import *


class EnfermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = MedicoSignUpForm
    template_name = 'Triagem/cria_enfEtec/cria_enfEtec.html'
    success_message = 'Usuário atualizado com sucesso.'
    success_url = reverse_lazy('Triagem:user_create')

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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object.user # adiciona o usuário atual ao formulário
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        grupo = self.request.POST.get('grupo')

        if grupo == 'group_Enfermagem':
            group = Group.objects.get(name='group_Enfermagem')
        elif grupo == 'group_Tec_Enfermagem':
            group = Group.objects.get(name='group_Tec_Enfermagem')

        custom_user = CustomUser.objects.get(user=self.object.user)
        custom_user.telefone = form.cleaned_data['telefone']
        custom_user.data_nascimento = form.cleaned_data['data_nascimento']
        custom_user.endereco = form.cleaned_data['endereco']
        custom_user.crm = form.cleaned_data['crm']
        custom_user.grupo = group
        custom_user.save()

        custom_user.user.groups.clear()
        custom_user.user.groups.add(group)

        return redirect(self.success_url)    
