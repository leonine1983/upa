
from Triagem.models import triagem
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Frame


from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from reportlab.lib.colors import PCMYKColor

from reportlab.lib.colors import Color, PCMYKColor
from reportlab.lib.pagesizes import A4
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Frame
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO
from django.http import HttpResponse
from Triagem.models import triagem
from datetime import datetime

from reportlab.graphics.shapes import Drawing, Rect
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

from reportlab.lib.colors import PCMYKColor
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer, Frame
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from django.http import HttpResponse
from Triagem.models import triagem
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle




    
def formatar_data(data):
    meses = {
        1: 'janeiro',
        2: 'fevereiro',
        3: 'março',
        4: 'abril',
        5: 'maio',
        6: 'junho',
        7: 'julho',
        8: 'agosto',
        9: 'setembro',
        10: 'outubro',
        11: 'novembro',
        12: 'dezembro',
    }

    dia = data.strftime('%d')
    mes = meses[data.month]
    ano = data.strftime('%Y')

    return "{} de {} de {}".format(dia, mes, ano)






from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import PCMYKColor
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from io import BytesIO
from django.http import HttpResponse

def add_header_footer(canvas, doc):
    # Função para adicionar o cabeçalho e o rodapé em todas as páginas do PDF
    image_path_top = 'media/sus_top.jpg'
    image_path_bottom = 'media/sus_bottom.jpg'
    logo_image_top = utils.ImageReader(image_path_top)
    logo_image_bottom = utils.ImageReader(image_path_bottom)
    logo_width_top, logo_height_top = logo_image_top.getSize()
    logo_width_bottom, logo_height_bottom = logo_image_bottom.getSize()

    # Adicionar o cabeçalho (imagem do topo) em todas as páginas
    canvas.drawImage(image_path_top, 50, doc.pagesize[1] - 70, width=logo_width_top*0.25, height=logo_height_top*0.25)

    # Adicionar o rodapé (imagem do rodapé e texto informativo) em todas as páginas
    canvas.drawImage(image_path_bottom, 72, 10, width=logo_width_bottom*0.2, height=logo_height_bottom*0.2)

    footer_text = "Relatório gerado pelo SG-UPA / CAUAN's Technology ™"
    canvas.saveState()
    canvas.setFont('Times-Roman', 7)
    canvas.drawString(375, 55, footer_text)

    # Adicionar o texto em parágrafo no rodapé
    footer_paragraph = Paragraph("<b>UPA VERA CRUZ</b><br/>Avenida Juvenal João Vinagre, 175, Centro, Vera Cruz - Ba<br/>Tel.: (71) 3633-2286<br/>Email: servicosocial.upaveracruz@gmail.com",
                                 getSampleStyleSheet()['Normal'])
    w, h = footer_paragraph.wrap(doc.width*5, doc.bottomMargin)
    footer_paragraph.drawOn(canvas, doc.leftMargin, h-40)

    canvas.restoreState()


def criar_pdf_fichas_de_atendimento(request):
    # Definindo a largura e altura da página A4
    width, height = A4

    # Criando um buffer para armazenar o PDF
    buffer = BytesIO()

    # Criando o objeto de documento para gerar o PDF
    doc = SimpleDocTemplate(buffer, pagesize=A4)

    # Estilo do título com background cinza
    title_style = ParagraphStyle(
        name='TitleStyle',
        parent=getSampleStyleSheet()['Normal'],
        fontSize=20,
        leading=24,
        textColor='white',
        backColor=PCMYKColor(0, 0, 0, 30),
        leftIndent=6,
        rightIndent=6,
    )

    # Estilo do parágrafo
    styles = getSampleStyleSheet()
    my_style = styles["Normal"]

    # Conteúdo do parágrafo de informações de registros de pacientes
    data = []

    # Obtendo os registros de triagem (ou ficha_de_atendimento, dependendo dos objetos)
    atendimentos = triagem.objects.filter(final_triagem_time = datetime.today(), paciente_triagem__triagem_concluida = 1)
    hoje = datetime.today()

    # Inicializando as variáveis de contagem
    quantidade_atendimentos = len(triagem.objects.filter(final_triagem_time = datetime.today(), paciente_triagem__triagem_concluida = 1))
    quantidade_masculino = len(triagem.objects.filter(paciente_triagem__paciente_envio_triagem__sexo = 1, final_triagem_time = datetime.today(), paciente_triagem__triagem_concluida = 1))
    quantidade_feminino = len(triagem.objects.filter(paciente_triagem__paciente_envio_triagem__sexo = 2, final_triagem_time = datetime.today(), paciente_triagem__triagem_concluida = 1))
    quantidade_criancas = 0
    quantidade_adultos = 0
    quantidade_idosos = 0

    # Preenchendo os dados no parágrafo e contando a quantidade de atendimentos
    for aten in atendimentos:
        content = [
            f"<br/>",
            f"<b>Data do atendimento:</b> {aten.paciente_triagem.data_envio_triagem} <b>| Horário:</b> {aten.paciente_triagem.horario_triagem}",
            f"<b>Nome Social:</b> {aten.paciente_triagem.paciente_envio_triagem.nome_social}",
            f"<b>Idade:</b> {aten.paciente_triagem.paciente_envio_triagem.idade} anos",
            f"<b>Data de Nascimento:</b> {formatar_data(aten.paciente_triagem.paciente_envio_triagem.data_nascimento)}",
            f"<b>Sexo:</b> {aten.paciente_triagem.paciente_envio_triagem.sexo}",
            f"<b>RG:</b> {aten.paciente_triagem.paciente_envio_triagem.RG}",
            f"<b>CPF:</b> {aten.paciente_triagem.paciente_envio_triagem.CPF}",
            f"<b>Nacionalidade:</b> {aten.paciente_triagem.paciente_envio_triagem.nacionalidade}",
            f"<b>Rua:</b> {aten.paciente_triagem.paciente_envio_triagem.rua}",
            f"<b>Bairro:</b> {aten.paciente_triagem.paciente_envio_triagem.bairro}",
            f"<b>Cidade:</b> {aten.paciente_triagem.paciente_envio_triagem.cidade}",
            f"<b>Estado:</b> {aten.paciente_triagem.paciente_envio_triagem.estado}",
            f"<b>País:</b> {aten.paciente_triagem.paciente_envio_triagem.pais}",
            f"<b>CEP:</b> {aten.paciente_triagem.paciente_envio_triagem.CEP}",
            f"<b>Nome da Mãe:</b> {aten.paciente_triagem.paciente_envio_triagem.nome_mae}",
            f"<b>Responsável:</b> {aten.paciente_triagem.paciente_envio_triagem.responsavel}",
            f"<b>Telefone:</b> {aten.paciente_triagem.paciente_envio_triagem.tel}",
            f"_______________________________________________________________________________",
            # Espaço entre os parágrafos
        ]
        data.extend(content)


    

      # Criando o parágrafo com os dados e aplicando estilos
    content_paragraph = Paragraph("<br/>".join(data), my_style)

    # Criando a tabela com os dados
    tabela_dados = Table([
        ["Resumo de Atendimentos", "Sexo M", "Sexo F", hoje],
        ["Quantidade de Crianças", quantidade_criancas],
        ["Quantidade de adultos", quantidade_masculino, quantidade_feminino],        
        ["Quantidade de Idosos", quantidade_idosos],
        ["Total de Atendimentos", quantidade_atendimentos],
    ])

    # Definindo estilos para a tabela
    style_table = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Cabeçalho cinza
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Texto branco no cabeçalho
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Alinhamento centralizado
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Fonte em negrito no cabeçalho
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  # Espaçamento inferior no cabeçalho
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Cor de fundo para as células de dados
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  # Borda da tabela
    ])

    # Aplicando o estilo à tabela
    tabela_dados.setStyle(style_table)

    # Adicionando a tabela à lista de elementos do PDF
    elements = [Spacer(1, 10),tabela_dados, content_paragraph]

    # Construindo o PDF com o conteúdo, o cabeçalho e o rodapé em todas as páginas
    doc.build(elements, onFirstPage=add_header_footer, onLaterPages=add_header_footer)

    # Obtendo os dados do buffer e fechando-o
    pdf_data = buffer.getvalue()
    buffer.close()

    # Criando uma resposta HTTP com o arquivo PDF
    response = HttpResponse(pdf_data, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=venue.pdf'
    response['Content-Type'] = 'application/pdf'
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    response['Content-Security-Policy'] = "default-src 'self'"
    response['X-Content-Type-Options'] = 'nosniff'

    return response  # Retorna o objeto HttpResponse com o arquivo PDF


def view_pdf_diario(request):
    registros = triagem.objects.all()
    pdf_content = criar_pdf_fichas_de_atendimento(registros)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="fichas_de_atendimento.pdf"'
    response.write(pdf_content.getvalue())

    return response

