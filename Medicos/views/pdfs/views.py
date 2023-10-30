#Cria os usuarios
from django.http import HttpResponse
from django.urls import  reverse_lazy
#restrição de acesso
#Libs para escrever html no pdf

from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
#Biblioteca para gerar pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.units import mm
from reportlab.lib.colors import black

from django.shortcuts import render, HttpResponse
from Triagem.models import triagem
from Atendimento.models import *
# views.py


# RECEITUARIO ----------------------------------------------------------------
# ----------------------------------------------------------------------------
def mp(mm):
    return mm/0.352777


def gerarPdf(request, pk):

    my_Style=ParagraphStyle('My Para style',
    fontName='Times-Roman',
    backColor='',
    fontSize=16,
    borderColor='',
    borderWidth=2,
    borderPadding=(20,20,20),
    leading=20,
    alignment=0
    )

    width,height=A4
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    c.drawImage("media/png/sus_top.png", mm(1),mm(258)) 
    c.drawImage("media/png/sus_bottom.png", mm(110),mm(1))
    
    # Add some lines of text / Adicionar algumas linhas de texto

    venues = triagem.objects.filter(pk = pk)
    lines = []
    

    for venue in venues:
        
        a = str(venue.paciente_triagem)         
        b = str(venue.preescrever_medicamento_medico)        
        p1=Paragraph(f'''<b> Nome do(a) paciente:</b><BR />\
            {a}<BR/>\
                <BR/>\
                    <BR/><BR/>\
                        <b>Preescrição de Medicamento:</b><BR/>\
                            <BR/>{b}\
                                <BR/><BR/><BR/><BR/>\
                                    <b>Nome do médico:</b><BR/>\
                                    <BR/>Dr.(a) {request.user}''',my_Style)  
    
    p2 = Paragraph(f'''\
        <b>UPA VERA CRUZ</b>\
            <BR/>Avenida Juvenal João Vinagre, 175, Centro, Vera Cruz - Ba\
            <BR/>Tel.: (71) 3633-2286\
            <BR/>Email: servicosocial.upaveracruz@gmail.com
                ''')
    p2.wrapOn(c, 300, 10)
    p2.drawOn(c, width-550, height-825)
       

    p1.wrapOn(c,480,10)
    p1.drawOn(c,width-550,height - 550)
    c.showPage()
    c.save()
    #buffer.seek(0)
    pdf_data = buffer.getvalue()
    buffer.close()

    #Envio o PDF como resposta HTTP com o tio de conteudo 'application/pdf'
    #return FileResponse(buf, as_attachment=True, filename='venue.pdf')
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=venue.pdf'
    response['Content-Type'] = 'application/pdf'
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Content-Security-Policy'] = "default-src 'self'"
    response['X-Content-Type-Options'] = 'nosniff'
    
    
