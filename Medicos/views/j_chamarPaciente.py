# Importar csv
import csv

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
#Cria os usuarios
from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import  redirect, render
from django.urls import  reverse_lazy
#restrição de acesso
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
#Libs para escrever html no pdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
#Biblioteca para gerar pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph


from django.shortcuts import render, HttpResponse
from io import BytesIO
from reportlab.lib.units import mm
from reportlab.lib.colors import black
from Triagem.models import triagem


from Atendimento.models import *
#from Medicos.forms import Form_medico_atendimento
from Medicos.models import CustomUser
from Triagem.models import triagem

import chardet
from Medicos.models import cid_10


from Medicos.models import CustomUser
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

# views.py
from django.contrib.auth.hashers import make_password
from Medicos.models import User

from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, CadastroSala, Salas_Atendimento


# ---------------------------------------------- END  ----------------------------------------------
def cadastrar_chamada(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome')
        print(f'Este é o nome do paciente: {nome_paciente}')
        print(f'Este é o ID do usuário: {request.user.id}')
        chamada = Chamar_P_para_atendimento(nome_paciente=nome_paciente, request=request)
        chamada.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})