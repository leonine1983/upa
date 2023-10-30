#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from Triagem.models import Classifica_risco_model


# Classificação de risco
class Classifica_risco_view(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Classifica_risco_model
    fields = ['classifica_tipo', 'descri']
    template_name = 'Triagem/classifica_risco.html'
    success_url = reverse_lazy('Triagem:triagem-enfermaria')
    success_message = "classificação de risco criada com sucesso!"


class Classifica_risco_lista_view(LoginRequiredMixin, ListView):
    model = Classifica_risco_model
    template_name =  'Triagem/classifica_risco.html'
    paginate_by =12


class Classifica_risco_Update_view(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Classifica_risco_model    
    fields = ['classifica_tipo', 'descri']
    template_name =  'Triagem/classifica_risco.html'
    success_url = reverse_lazy('Triagem:classifica-risco-lista')
    success_message = "Classificação de risco atualizada com sucesso!"
