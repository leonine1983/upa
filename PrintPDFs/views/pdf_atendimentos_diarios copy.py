
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


def add_footer(canvas, doc):
    # Função para adicionar o rodapé em todas as páginas do PDF
    footer_text = "Relatório gerado pelo SG-UPA / CAUAN's Technology ™"
    canvas.saveState()
    canvas.setFont('Times-Roman', 7)
    canvas.drawString(375, 55, footer_text)

    

    # Adicionando a imagem no rodapé
    image_path = 'media/sus_bottom.jpg'
    logo_image = utils.ImageReader(image_path)
    logo_width, logo_height = logo_image.getSize()
    canvas.drawImage(image_path, 72, 10, width=logo_width*0.2, height=logo_height*0.2)


    # Adicionando o texto em parágrafo no rodapé
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

    # Adicionando a imagem no topo do PDF
    image_path = 'media/sus_top.jpg'
    logo_image = utils.ImageReader(image_path)
    logo_width, logo_height = logo_image.getSize()
    logo = Image(image_path, width=logo_width * 0.3, height=logo_height * 0.3)  # Ajuste o tamanho da imagem conforme necessário

      


     # Título da página
    title_text = "<b>RELATÓRIO GERAL DO SISTEMA | Resumo</b>"
    title = Paragraph(title_text, title_style)

    # Cabeçalho da página
    header_text = "<b>UPA VERA CRUZ</b><br/>Avenida Juvenal João Vinagre, 175, Centro, Vera Cruz - Ba<br/>Tel.: (71) 3633-2286<br/>Email: servicosocial.upaveracruz@gmail.com"
    header = Paragraph(header_text, my_style)

    # Adicionando o espaço abaixo da imagem
    image_with_space = [logo, Spacer(1, 20), title, Spacer(1,20)]

    # Conteúdo do parágrafo de informações de registros de pacientes
    data = []

    # Obtendo os registros de triagem (ou ficha_de_atendimento, dependendo dos objetos)
    atendimentos = triagem.objects.all()

    # Preenchendo os dados no parágrafo
    for aten in atendimentos:
        content = [
            f"<br/>",
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

    # Criando o rodapé com informações adicionais
    footer_style = ParagraphStyle(
        name='FooterStyle',
        parent=getSampleStyleSheet()['Normal'],
        fontSize=8,
        textColor='gray',
    )
    

    # Construindo o PDF com o título no retângulo cinza   
    # Construindo o PDF com a imagem, o título e o rodapé
    doc.build(image_with_space + [header, content_paragraph], onFirstPage=add_footer, onLaterPages=add_footer)
 
    # doc.build(image_with_space + [header, content_paragraph])
    #doc.build([logo, title, header, content_paragraph])

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

