
from django.contrib import admin
from django.urls import path, include
from .views import gerarPdf, view_pdf_diario

app_name = 'PrintPDFs'

urlpatterns = [
    path  ('pdf/total_sistema', gerarPdf, name='quantiPacientSistema'),
    path ('pdf/atendimentos_diarios', view_pdf_diario, name='download_pdf')
    
]
