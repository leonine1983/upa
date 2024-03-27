from django.contrib.auth.decorators import login_required
#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView

from Atendimento.models import ficha_de_atendimento
from django.shortcuts import redirect
from django import forms
from django.contrib.auth.models import Group


class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)

        #self.fields['codigo_pacient'].widget.attrs['disabled'] = 'disabled'
        self.fields['codigo_pacient'].required = False
  

    class Meta:
        model = ficha_de_atendimento
        fields = ['nome_social', 'codigo_pacient', 'data_nascimento', 'sexo', 'etnia', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado', 'pais', 'CEP', 'nome_mae',  'tel', 'cartao_sus']

        widgets = {
            'nome_social': forms.TextInput(attrs={'class': 'form-control '}),
            #'nome_completo': forms.TextInput(attrs={'class': 'form-control '}),
            'codigo_pacient': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}),
            'sexo': forms.Select(attrs={'class': 'form-select '}),
            'etnia': forms.Select(attrs={'class': 'form-select '}),
            'RG': forms.TextInput(attrs={'class': 'form-control'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control '}),
            'rua': forms.TextInput(attrs={'class': 'form-control text-uppercase'}),
            'bairro': forms.Select(attrs={'class': 'form-select '}),
            'cidade': forms.Select(attrs={'class': 'form-select '}),
            'estado': forms.Select(attrs={'class': 'form-select '}),
            'pais': forms.Select(attrs={'class': 'form-select '}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control '}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control '}),
            'tel': forms.TextInput(attrs={'class': 'form-control '}),
            'cartao_sus': forms.TextInput(attrs={'class': 'form-control'}),
        }



class paciente_atualizar(LoginRequiredMixin, UpdateView):
    model = ficha_de_atendimento
    form_class = PacienteForm
    #fields = ['nome_social', 'data_nascimento','sexo', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado','CEP', 'nome_mae', 'responsavel', 'tel', 'cartao_sus'] 
    template_name = 'Atendimento/cadastro_paciente.html'    
    def get_success_url(self) :
        usuario_ativo = self.request.user
        user_groups = Group.objects.filter(user = usuario_ativo)
        for item in user_groups:
            user_groups = item.name
            if user_groups == 'group_UPA-Admin' or user_groups == 'group_Medicos':
                success_url = reverse_lazy("Medicos:lista_paciente_medico") 
            else:
                success_url = reverse_lazy("Atendimento:lista-paciente") 
            return success_url
    
    
    

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
    
    def form_valid(self, form):
        if self.request.user.first_name:
            form.instance.nome_recepcionista =f'{self.request.user.first_name} {self.request.user.last_name}'
        else:
            form.instance.nome_recepcionista = self.request.user.username
        return super().form_valid(form)
    