from django.shortcuts import render, HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import black
from reportlab.platypus import Paragraph, Table, TableStyle
from Atendimento.models import ficha_de_atendimento
from Medicos.models import CustomUser

def mp(mm):
    return mm/0.352777


def gerarPdf(request):

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
    #c.drawImage("media/png/sus_top.png", mp(1),mp(258)) 
    #c.drawImage("media/png/sus_bottom.png", mp(110),mp(1))
    
    # Add some lines of text / Adicionar algumas linhas de texto

    venues = ficha_de_atendimento.objects.all()
    venues_M = ficha_de_atendimento.objects.filter(sexo = 1).count()
    venues_F = ficha_de_atendimento.objects.filter(sexo = 2).count()
    venues_cidade = ficha_de_atendimento.objects.filter(cidade = 1).count()
    venues_Notcidade = ficha_de_atendimento.objects.exclude(cidade = 1).count()
    total_Registros = venues.count()

    # Cabeçalho pagina -------------------------------------------------------------------
    title = [['RELATÓRIO GERAL DO SISTEMA | Resumo ']]

    title_table = Table(title, colWidths=[550], minRowHeights=[50])
    title_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), (0.5, 0.5, 0.5)), 
        ('TEXTCOLOR', (0, 0), (-1, -1), (1, 1, 1)),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('FONTSIZE', (0,0), (0,0), 16)
    ]))
    title_table.wrapOn(c, width-50, height-50)
    title_table.drawOn(c, 25, height-125)

    # Rodape da pagina -------------------------------------------------------------------
    p2 = Paragraph(f'''\
        <b>UPA VERA CRUZ</b>\
            <BR/>Avenida Juvenal João Vinagre, 175, Centro, Vera Cruz - Ba\
            <BR/>Tel.: (71) 3633-2286\
            <BR/>Email: servicosocial.upaveracruz@gmail.com
                ''')
    
    # Tabela de informações de registros de pacientes ---------------------------------------------------------------

    data = [['Registros de pacientes no Sistema', 'Quantidade']]
    data.append(['Nº total de registros de pacientes:', total_Registros] )
    data.append(['Quantidade pessoas do sexo masculino', venues_M])
    data.append(['Quantidade pessoas do sexo feminino', venues_F])
    data.append(['Quantidade registros de pessoas moradores no município de Vera Cruz', venues_cidade])
    data.append(['Quantidade registros de pessoas moradores em outros municípios', venues_Notcidade])
    """for venue in venues:
        data.append([venue.nome_social, venue.idade, venue.sexo])"""

    table = Table(data)
    table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), (0, 0, 0)),
    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #('BACKGROUND', (0, 1), (-1, -1), (245, 245, 245)),
    ('GRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ]))

    table.wrapOn(c, width-50, height-50)
    table.drawOn(c, 25, height-260)

    # Tabela de informações de Usuarios ---------------------------------------------------------------
    model_user = CustomUser.objects.all().count()
    model_user_admin = CustomUser.objects.filter(grupo_id__name = 'group_UPA-Admin').count()
    model_user_medicos = CustomUser.objects.filter(grupo_id__name = 'group_Medicos').count()
    model_user_enfermeiros = CustomUser.objects.filter(grupo_id__name = 'group_Enfermagem').count()
    model_user_tec = CustomUser.objects.filter(grupo_id__name = 'group_Tec_Enfermagem').count()

   
    data_user = [['Registro de usuários no Sistema', 'Quantidade']]
    data_user.append(['Nº total de usuarios cadastrados', model_user] )
    data_user.append(['Quantidade de Administradores', model_user_admin] )
    data_user.append(['Quantidade de Medicos', model_user_medicos] )
    data_user.append(['Quantidade de Enfermeiras', model_user_enfermeiros] )
    data_user.append(['Quantidade de Técnicos em Enfermagem', model_user_tec] )
    data_user_table = Table(data_user)
    data_user_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), (0, 0, 0)),
    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #('BACKGROUND', (0, 1), (-1, -1), (245, 245, 245)),
    ('GRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ]))

    data_user_table.wrapOn(c, width-50, height-50)
    data_user_table.drawOn(c, 25, height-400)

# Tabela de informações de Atendimentos ---------------------------------------------------------------
    model_user = CustomUser.objects.all().count()
    model_user_admin = CustomUser.objects.filter(grupo_id__name = 'group_UPA-Admin').count()
    model_user_medicos = CustomUser.objects.filter(grupo_id__name = 'group_Medicos').count()
    model_user_enfermeiros = CustomUser.objects.filter(grupo_id__name = 'group_Enfermagem').count()
    model_user_tec = CustomUser.objects.filter(grupo_id__name = 'group_Tec_Enfermagem').count()

   
    data_user = [['Registro de usuários no Sistema', 'Quantidade']]
    data_user.append(['Nº total de usuarios cadastrados', model_user] )
    data_user.append(['Quantidade de Administradores', model_user_admin] )
    data_user.append(['Quantidade de Medicos', model_user_medicos] )
    data_user.append(['Quantidade de Enfermeiras', model_user_enfermeiros] )
    data_user.append(['Quantidade de Técnicos em Enfermagem', model_user_tec] )
    data_user_table = Table(data_user)
    data_user_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), (0, 0, 0)),
    ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #('BACKGROUND', (0, 1), (-1, -1), (245, 245, 245)),
    ('GRID', (0, 0), (-1, -1), 0.25, (0, 0, 0)),
    ]))

    data_user_table.wrapOn(c, width-50, height-50)
    data_user_table.drawOn(c, 25, height-540)


    p2.wrapOn(c, 300, 10)
    p2.drawOn(c, width-550, height-825)

    c.showPage()
    c.save()
    #buffer.seek(0)
    pdf_data = buffer.getvalue()
    buffer.close()

    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=venue.pdf'
    response['Content-Type'] = 'application/pdf'
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Content-Security-Policy'] = "default-src 'self'"
    response['X-Content-Type-Options'] = 'nosniff'

    return response  # retorna o objeto HttpResponse com o arquivo PDF
   

