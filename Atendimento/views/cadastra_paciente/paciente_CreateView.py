from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import ficha_de_atendimento
from django.shortcuts import redirect
from django import forms
import uuid

import random

import random

import random

class PacienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PacienteForm, self).__init__(*args, **kwargs)

        codigo_aleatorio = self.gerar_codigo_aleatorio()
        while ficha_de_atendimento.objects.filter(codigo_pacient=codigo_aleatorio).exists():
            codigo_aleatorio = self.gerar_codigo_aleatorio()

        self.fields['codigo_pacient'].initial = codigo_aleatorio
        #self.fields['codigo_pacient'].widget.attrs['disabled'] = 'disabled'
        self.fields['codigo_pacient'].required = False

    def gerar_codigo_aleatorio(self):
        codigo_inteiro = random.randint(0, 99999)
        codigo_formatado = "{:05d}-{:02d}".format(codigo_inteiro // 100, codigo_inteiro % 100)
        return codigo_formatado

    class Meta:
        model = ficha_de_atendimento
        fields = ['nome_social', 'codigo_pacient', 'data_nascimento', 'sexo', 'etnia', 'RG', 'CPF', 'nacionalidade', 'rua', 'bairro', 'cidade', 'estado', 'pais', 'CEP', 'nome_mae', 'responsavel', 'tel', 'cartao_sus']

        widgets = {
            'nome_social': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_pacient': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
            'sexo': forms.Select(attrs={'class': 'form-select'}),
            'RG': forms.TextInput(attrs={'class': 'form-control'}),
            'CPF': forms.TextInput(attrs={'class': 'form-control'}),
            'nacionalidade': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.Select(attrs={'class': 'form-select'}),
            'bairro': forms.Select(attrs={'class': 'form-select'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'nome_mae': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'cartao_sus': forms.TextInput(attrs={'class': 'form-control'}),
        }



        

class paciente_cadastro(LoginRequiredMixin, CreateView):
    model = ficha_de_atendimento
    form_class = PacienteForm
    template_name = 'Atendimento/cadastro_paciente.html'

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        url = reverse_lazy('Atendimento:envio_paciente_a_triagem_2', args=[self.object.pk])
        print('ID do objeto criado:', self.object.pk)
        return url
    
     #Se o usuario nao estiver logado
    login_url = reverse_lazy('Access_Login:access_login_page')
    redirect_field_name = 'next'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect (self.login_url + '?next=' + request.path)
        return super().dispatch(request, *args, **kwargs)