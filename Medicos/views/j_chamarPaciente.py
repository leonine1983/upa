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

from Atendimento.models import *
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento

def cadastrar_chamada(request):
    if request.method == 'POST':
        nome_paciente = request.POST.get('nome')
        chamada = Chamar_P_para_atendimento(nome_paciente=nome_paciente, request=request)
        chamada.save()
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})