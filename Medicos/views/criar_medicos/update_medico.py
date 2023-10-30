from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import  reverse_lazy
from django.views.generic import UpdateView
from Atendimento.models import *
from Medicos.models import CustomUser
from django import forms

# views.py
from django.contrib.auth.hashers import make_password
from Medicos.models import User


class MedicoFormUpdate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email',]

    def save(self, commit=True):
        user = super(MedicoFormUpdate, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class MedicoUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = MedicoFormUpdate
    template_name = 'Medicos/criar_medicos/update.html'
    success_url = reverse_lazy('Medicos:medico_signup')

    def get_context_data(self, **kwargs):
        medicos_group = Group.objects.get(name='group_Medicos')
        users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'user__id', 'id','user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )


        context = super().get_context_data(**kwargs)
        context["user_update"] =User.objects.filter(pk = self.kwargs['pk'])
        context["users"] = users
        context["user_edit"] = 'user_edit'
        
        return context
