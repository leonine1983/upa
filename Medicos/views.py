from datetime import datetime
from io import BytesIO

# Importar csv
import csv

#restringir acesso
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
#Cria os usuarios
from django.contrib.auth.models import Group, User
from django.http import FileResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
#restrição de acesso
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView
#Libs para escrever html no pdf
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
#Biblioteca para gerar pdf
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

from Atendimento.models import *
#from Medicos.forms import Form_medico_atendimento
from Medicos.models import CustomUser, Medico_atendimento
from Triagem.models import triagem
from datetime import datetime



# Essa View, retorna a lista de pacientes que passaram pela Triagem e aguardam atendimento médico.
@login_required
def medico_protuario_view_(request):
    triagem_filtro = triagem.objects.exclude(final_medico_atendimento = 1)
    return render(request, 'Medicos/medico.html', {
        'n_pacientes_triagem': len(triagem_filtro),
        'object_list' : triagem_filtro 
    })


def medico_atendimento_view(request, pk):
    dados_triagem = triagem.objects.filter(pk=pk)
    for dados in dados_triagem:
        #tempo1 =datetime(dados.hora_triagem)
        dados = dados.paciente_triagem_id        
        dados_triagem = envio_triagem.objects.filter(pk=dados) 
        info_Hora_Tri = triagem.objects.filter(paciente_triagem_id=dados)
        for t in info_Hora_Tri:
            info_Hora_envioT = t.hora_triagem

        #hora_triagem = datetime.strptime(dados.hora_triagem, '%Y-%m-%d %H:%M:%S')
        #print(f'Esse é o horario da triagem {hora_triagem}')
        

    dados_envio_triagem = envio_triagem.objects.filter(pk=dados)
    for dados in dados_envio_triagem:
        #tempo2 =time(dados.horario_triagem)
        dados = dados.paciente_envio_triagem_id 
        info_Hora_envioT = envio_triagem.objects.filter(paciente_envio_triagem_id = dados)
        for t in info_Hora_envioT:
            info_Hora_envioT = t.horario_triagem

    #contem o horário da triagem
    info_Hora_envioT

    #contem o horário do envio_triagem
    info_Hora_envioT
        
        #print (f'essa e a informação: {info_Hora_envioT}')
        #horario_triagem = datetime.strptime(dados.horario_triagem, '%Y-%m-%d %H:%M:%S')
        #print(f'Essé e o horario de envio para a triagem {hora_triagem}')
   

    # converter as strings em objetos datetime
    

    # calcular a diferença em minutos
    #print(f'o tempo e minutos é {diferenca_minutos}')


    #tempo = tempo2 - tempo1     
        
    return render(request, 'Medicos/medico_atendimento.html', {
        'paciente_triagem' : triagem.objects.filter(pk=pk), 
        'ficha_atendimento' : ficha_de_atendimento.objects.filter(pk=dados),
        'dados_triagem' : dados_triagem,
        #'tempo' : tempo         
    } )


class atendimento_medico_createView(LoginRequiredMixin, CreateView):
    model = Medico_atendimento
    #Chave Estrangeira 'paciente_medico_atendimento'
    fields = ['paciente_medico_atendimento', 'historico_doenca_atual_HDA', 'exame_fisico', 'Diagnostico', 'classificacao_internacional_doenca_CID', 'conduta']
    template_name = 'Medicos/medico_atendimento_atendimento.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 

        pk = self.kwargs['pk']    
        
        context['triagem'] = triagem.objects.filter(id = pk)
        
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.medico_nome = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    

    
    #success_url = reverse_lazy('Medicos:dados do paciente_medicamentos self.kwargs['pk']')
    def get_success_url(self):
        return reverse('Medicos:dados do paciente_medicamentos', kwargs={'pk':self.kwargs['pk']})


class atendimento_medico_updateview(LoginRequiredMixin, UpdateView):
    model = triagem
    #Chave Estrangeira 'paciente_medico_atendimento'
    fields = ['preescrever_medicamento_medico', 'enviar_ambulatorio','encaminhamento', 'atestado', 'exames']   
    template_name = 'Medicos/prescrever-medicamento.html'

    def get_success_url(self):
        envio_filter = self.kwargs['pk']
        triagem_filter = triagem.objects.filter(id = envio_filter)
        for n in triagem_filter:
            key = n.id
            data_key = n.data_triagem        

        return reverse('Medicos:exibe_prescreve_medicamento', kwargs={'pk':key})


class atendimento_medico_concluido_update(LoginRequiredMixin, UpdateView):
    model = triagem
    fields = ['final_medico_atendimento']
    template_name = 'Medicos/confirma_final.html'
    success_url =reverse_lazy('Medicos:medico_prontuario')


#View que exibe o medicamento receitado pelo medico
class exibe_prescreve_medicamento_update(LoginRequiredMixin, DetailView):
    model = triagem
    template_name = 'Medicos/exibir_impressao/exibi_prescreve_medicamento.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        triagem_now = triagem.objects.filter(pk= self.kwargs['pk'])
        cid10 = Medico_atendimento.objects.filter(paciente_medico_atendimento = self.kwargs['pk'])
        print(cid10)
        context = {
            'triagem_now':triagem_now,
            'cid10': cid10
        }

        return context
    

# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx PDFs xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# RECEITUARIO ----------------------------------------------------------------
# ----------------------------------------------------------------------------
def mp(mm):
    return mm/0.352777


def gerarPdfdd(request, pk):

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
    c.drawImage("media/png/sus_top.png", mp(1),mp(258)) 
    c.drawImage("media/png/sus_bottom.png", mp(110),mp(1))
    
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
    return response



from django.shortcuts import render, HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import black
from reportlab.platypus import Paragraph
from .models import triagem


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
   


# ATESTADO -------------------------------------------------------------------
# ----------------------------------------------------------------------------
def gerarPdf_atestado(request, pk):

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
   


#------------------------Cria perfil completo de paciente ---------------------------
@login_required
def paciente_perfil_completo(request, pk):

    #faço uma busca no model triagem
    dados = triagem.objects.filter(id = pk)
    for d in dados:
        paciente_triagem = d.paciente_triagem_id
        pkk = d.id
    
    dados = envio_triagem.objects.filter(id = paciente_triagem)
    for d in dados:
        paciente = d.paciente_envio_triagem_id
    
    dados = ficha_de_atendimento.objects.filter(id = paciente)
    for d in dados:
        paciente_id = d.id
        paciente_nome = d.nome_social
        paciente_sexo = d.sexo.id
        paciente_sexo_str = d.sexo
        paciente_idade = d.idade
        paciente_nascimento = d.data_nascimento
        paciente_rg = d.RG
        paciente_cpf = d.CPF
        paciente_nacio = d.nacionalidade
        paciente_rua = d.rua
        paciente_bairro = d.bairro
        paciente_cidade = d.cidade
        paciente_estado = d.estado
        paciente_cep = d.CEP
        paciente_mae = d.nome_mae
        paciente_resp = d.responsavel
        paciente_tel = d.tel
        paciente_data_cadast = d.data_cadastro
        paciente_horari_cadast = d.horario_cadastro
        paciente_sus = d.cartao_sus     
  
    return render(request, 'Medicos/perfis/perfil-paciente_completo.html', {
        #Dados da ficha do paciente
        'paciente' : dados,
        'paciente_nome': paciente_nome,
        'paciente_sexo' : paciente_sexo,
        'paciente_sexo_str' : paciente_sexo_str,
        'paciente_idade' : paciente_idade,
        'paciente_nascimento' : paciente_nascimento,
        'paciente_rg' : paciente_rg,
        'paciente_cpf' : paciente_cpf,
        'paciente_nacio' : paciente_nacio,
        'paciente_rua' : paciente_rua,
        'paciente_bairro' : paciente_bairro,
        'paciente_cidade' : paciente_cidade,
        'paciente_estado' : paciente_estado,
        'paciente_cep' : paciente_cep,
        'paciente_mae' : paciente_mae,
        'paciente_resp' : paciente_resp,
        'paciente_tel' : paciente_tel,
        'paciente_data_cadast' : paciente_data_cadast,
        'paciente_horari_cadast' : paciente_horari_cadast,
        'paciente_sus' : paciente_sus,
        'pkK': pkk 
        #'lista': envio_triagem_id
    })


 # -------------------Cria perfil completo de paciente SEGUNDA PARTE ------------------------------------
@login_required
def paciente_perfil_completo_segunda_parte(request, pk):

    #faço uma busca no model triagem
    dados = triagem.objects.filter(id = pk)
    for d in dados:
        paciente_triagem = d.paciente_triagem_id
        pkk = d.id
    
    dados = envio_triagem.objects.filter(id = paciente_triagem)
    for d in dados:
        paciente = d.paciente_envio_triagem_id

    #Dados contem o id do paciente
    dados = ficha_de_atendimento.objects.filter(id = paciente)
    for d in dados:
        paciente_id = d.id
        paciente_nome = d.nome_social
        paciente_sexo = d.sexo.id
        paciente_sexo_str = d.sexo
        paciente_idade = d.idade
        paciente_nascimento = d.data_nascimento
        paciente_rg = d.RG
        paciente_cpf = d.CPF
        paciente_nacio = d.nacionalidade
        paciente_rua = d.rua
        paciente_bairro = d.bairro
        paciente_cidade = d.cidade
        paciente_estado = d.estado
        paciente_cep = d.CEP
        paciente_mae = d.nome_mae
        paciente_resp = d.responsavel
        paciente_tel = d.tel
        paciente_data_cadast = d.data_cadastro
        paciente_horari_cadast = d.horario_cadastro
        paciente_sus = d.cartao_sus  

    link_envio_triagem = envio_triagem.objects.select_related('paciente_envio_triagem').filter(paciente_envio_triagem_id=paciente)
    link_triagem = pkk

    link_medico = Medico_atendimento.objects.select_related('paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem').filter(paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem_id=paciente)
   
        


    return render(request, 'Medicos/perfis/perfil-paciente_completo_segunda_parte.html', {
        #Dados da ficha do paciente
        'paciente' : dados,
        'paciente_nome': paciente_nome,
        'paciente_sexo' : paciente_sexo,
        'paciente_sexo_str' : paciente_sexo_str,
        'paciente_idade' : paciente_idade,
        'paciente_nascimento' : paciente_nascimento,
        'paciente_rg' : paciente_rg,
        'paciente_cpf' : paciente_cpf,
        'paciente_nacio' : paciente_nacio,
        'paciente_rua' : paciente_rua,
        'paciente_bairro' : paciente_bairro,
        'paciente_cidade' : paciente_cidade,
        'paciente_estado' : paciente_estado,
        'paciente_cep' : paciente_cep,
        'paciente_mae' : paciente_mae,
        'paciente_resp' : paciente_resp,
        'paciente_tel' : paciente_tel,
        'paciente_data_cadast' : paciente_data_cadast,
        'paciente_horari_cadast' : paciente_horari_cadast,
        'paciente_sus' : paciente_sus,
        'link_triagem' : link_triagem,        
        'link_envio_triagem' : link_envio_triagem,
        'link_medico' : link_medico,
        'pkK': pkk 
        #'lista': envio_triagem_id
    })


#lista de paciente e pesquisa com dados do historico
class paciente_lista_historico(ListView):
    model = ficha_de_atendimento
    template_name = 'Medicos/perfis/pacientes.html'
    paginate_by = 10
    
    #Fazer a pesquisa
    def get_queryset(self):
        txt_nome = self.request.GET.get('busca-paciente')

        if txt_nome:
            nome = ficha_de_atendimento.objects.filter(nome_social__icontains = txt_nome) | ficha_de_atendimento.objects.filter(cartao_sus__icontains = txt_nome)
    
        else:
            nome = ficha_de_atendimento.objects.all()

        return nome

    def form_valid(self, form):  
        form.instance.usuario = self.request.user

        url = super().form_valid(form)
        return url


# Essa view replicam o perfil do paciente, e do link visivel aos medicos
# e recebem o id a partir da ficha de atendimento ao inves de triagem
@login_required
def paciente_perfil_completo_menu_lateral(request, pk):
    dados = envio_triagem.objects.filter(paciente_envio_triagem_id=pk)
    if dados.exists():
        for d in dados:
            dados = triagem.objects.filter(paciente_triagem_id = d.id)
            for d in dados:
                pkk = d.id
                data_t = d.data_triagem
    else:
        pkk = 0 
        data_t = 0

    
    paciente = pk
    
    dados = ficha_de_atendimento.objects.filter(id = paciente)
    for d in dados:
        paciente_id = d.id
        paciente_nome = d.nome_social
        paciente_sexo = d.sexo.id
        paciente_sexo_str = d.sexo
        paciente_idade = d.idade
        paciente_nascimento = d.data_nascimento
        paciente_rg = d.RG
        paciente_cpf = d.CPF
        paciente_nacio = d.nacionalidade
        paciente_rua = d.rua
        paciente_bairro = d.bairro
        paciente_cidade = d.cidade
        paciente_estado = d.estado
        paciente_cep = d.CEP
        paciente_mae = d.nome_mae
        paciente_resp = d.responsavel
        paciente_tel = d.tel
        paciente_data_cadast = d.data_cadastro
        paciente_horari_cadast = d.horario_cadastro
        paciente_sus = d.cartao_sus     
  
    return render(request, 'Medicos/perfis/perfil-paciente_completo.html', {
        #Dados da ficha do paciente
        'paciente' : dados,
        'paciente_nome': paciente_nome,
        'paciente_sexo' : paciente_sexo,
        'paciente_sexo_str' : paciente_sexo_str,
        'paciente_idade' : paciente_idade,
        'paciente_nascimento' : paciente_nascimento,
        'paciente_rg' : paciente_rg,
        'paciente_cpf' : paciente_cpf,
        'paciente_nacio' : paciente_nacio,
        'paciente_rua' : paciente_rua,
        'paciente_bairro' : paciente_bairro,
        'paciente_cidade' : paciente_cidade,
        'paciente_estado' : paciente_estado,
        'paciente_cep' : paciente_cep,
        'paciente_mae' : paciente_mae,
        'paciente_resp' : paciente_resp,
        'paciente_tel' : paciente_tel,
        'paciente_data_cadast' : paciente_data_cadast,
        'paciente_horari_cadast' : paciente_horari_cadast,
        'paciente_sus' : paciente_sus,
        'pkK': pkk, 
        'data_t' : data_t
        #'lista': envio_triagem_id
    }) 


#-------------CRIAR USUARIO MEDICO ----------------
#-----------------------------------------------------------
# apos importar as classes necessárias do Django:
    # from django.contrib.auth.forms import UserCreationForm
    # from django.urls import reverse_lazy
    # from django.views.generic.edit import CreateView
    # from django.contrib.auth.models import Group

# 1 Crie uma classe de formulário que estenda o UserCreationForm do Django:


#2 Crie uma classe de visualização que estenda o CreateView do Django e 
# especifique o modelo do usuário a ser usado, o formulário a ser usado
# e a URL de sucesso:

from django import forms
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render

#from .forms import MedicoSignUpForm
from .models import CustomUser


class MedicoSignUpForm(forms.ModelForm):
    telefone = forms.CharField(max_length=20)
    
    data_nascimento = forms.DateField()

    endereco = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o nome da rua'}), label='Rua')
    crm = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o CRM'}), label="CRM")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'crm', 'endereco')




# Cria USUARIOS do tipo MEDICOS ----------------------------------------------
def medico_signup(request):
    if request.method == 'POST':
        form = MedicoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            group = Group.objects.get(name='group_Medicos')

            custom_user = CustomUser.objects.create(
                user=user,
                telefone=form.cleaned_data['telefone'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                endereco=form.cleaned_data['endereco'],
                crm=form.cleaned_data['crm'],  # novo campo
                grupo=group
            )

            group.user_set.add(user)  # Adiciona o usuário ao grupo
            messages.success(request, 'Usuário criado com sucesso.')
            return redirect('Medicos:medico_signup')
    else:
        form = MedicoSignUpForm()

    # Aqui, você pode incluir os campos adicionais na consulta ao banco de dados
    medicos_group = Group.objects.get(name='group_Medicos')
    users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'id','user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )
    

    return render(request, 'Medicos/criar_medicos/criar_medico.html', {
        'form': form,
        'users': users,
    })





from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.forms.widgets import PasswordInput

from .models import CustomUser

# views.py
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from .models import CustomUser

from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class MedicoFormUpdate(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email',]

    def save(self, commit=True):
        user = super(MedicoFormUpdate, self).save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class MedicoUpdateView(UpdateView):
    model = User
    form_class = MedicoFormUpdate
    template_name = 'Medicos/criar_medicos/criar_medico.html'
    success_url = reverse_lazy('Medicos:medico_signup')

    def get_context_data(self, **kwargs):
        medicos_group = Group.objects.get(name='group_Medicos')
        users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'user__id', 'id','user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )


        context = super().get_context_data(**kwargs)
        context["user_update"] =User.objects.filter(pk = self.kwargs['pk'])
        context["users"] = users
        context["user_edit"] = 'user_edit'
        
        return context

    
class MedicoUpdateView_extra(UpdateView):
    model = CustomUser
    fields = ['telefone', 'data_nascimento', 'endereco', 'crm']
    template_name = 'Medicos/criar_medicos/criar_medico.html'
    success_url = reverse_lazy('Medicos:medico_signup')

    def get_context_data(self, **kwargs):
        medicos_group = Group.objects.get(name='group_Medicos')
        users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'user__id', 'id','user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )


        context = super().get_context_data(**kwargs)
        context["user_update"] =CustomUser.objects.filter(pk = self.kwargs['pk'])
        context["users"] = users
        context["custom"] = 'custom'
        return context
    
   


class MedicoDeleteView(DeleteView):
    model = CustomUser
    template_name = 'Medicos/excluir_medicos/excluir_medico.html'
    success_url = reverse_lazy('Medicos:medico_signup')


# ---------------------------------------------- END  ----------------------------------------------


from django.shortcuts import render
from django.http import JsonResponse
from .models import Chamar_P_para_atendimento, CadastroSala, Salas_Atendimento



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



#SALAS -----------------------------------------------------------------------------
class Cadastra_Sala_view(LoginRequiredMixin, CreateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    fields = ['nome_Sala', 'descricao_Sala']
    success_url = reverse_lazy('Medicos:salas')


class Atualiza_Sala_UpdatView(LoginRequiredMixin, UpdateView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    fields = ['nome_Sala', 'descricao_Sala']
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = 'update'
        return context


class Lista_Salas_ListView(LoginRequiredMixin, ListView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['profissionais'] = Salas_Atendimento.objects.all()
        return context


class Delete_Sala_Delet(LoginRequiredMixin, DeleteView):
    model = CadastroSala
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')
    context_object_name = 'nomeSala'


# Vicula Medico às SALAS -----------------------------------------------------------------------------
class VinculaProfissiona_sala_view(LoginRequiredMixin, CreateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSala'
        return context

class VinculaProfissiona_sala_update(LoginRequiredMixin, UpdateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSalaUpdate'
        return context
    

class DeleteProfissionaSala_Delet(LoginRequiredMixin, DeleteView):
    model = Salas_Atendimento
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salas')
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context ['DeleteVinculo'] = 'DeleteVinculo'
        return context
    
    
# -----------------Controle de doenças CID 10 ---------------------------
import csv
import chardet
from .models import cid_10
from django.shortcuts import render
import datetime

import csv
import chardet
from django.shortcuts import render
from .models import cid_10

import csv
import sqlparse
from .models import cid_10
import chardet

import csv

def import_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        print(request.POST)  # Adicionando este print
        # Detecta o encoding do arquivo
        encoding = chardet.detect(csv_file.read())['encoding']
        csv_file.seek(0)
        decoded_file = csv_file.read().decode(encoding).splitlines()
        reader = csv.DictReader(decoded_file, delimiter=';')
        print(reader.fieldnames)
        
        inserts = []
        for row in reader:
            codigo = row['Codigo']
            if not cid_10.objects.filter(codigo=codigo).exists():
                obj = cid_10.objects.create(
                    codigo=codigo,
                    descricao=row['Descricao'],
                    codigo_Cid10=row['Codigos_da_CID_10']
                )
                inserts.append(str(obj))

        print(f"Linhas salvas: {len(inserts)}")
        return render(request, 'Medicos/import_csv.html', {'success': True})
    
    return render(request, 'Medicos/import_csv.html')






