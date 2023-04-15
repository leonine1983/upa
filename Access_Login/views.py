from email import message
from pyexpat.errors import messages
from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from forms.login import LoginForm
#Para fazer a autenticação vamos importar as seguintes bibliotecas
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#Para impedir que acessem as paginas sem está logado usamos LOGIN_REQUIRED
from django.contrib.auth.decorators import login_required
from Medicos.models import Salas_Atendimento


# Create your views here.
def access_login(request):
    form = LoginForm()
    if logout:
        messages.error(request, 'Você não está logado')

    return render(request, 'Access_Login/login.html',  {
        'form' : form,
        'form_action' : reverse('Access_Login:login_create')
    }
    )

#----------------VALIDAÇÃO ----------------------------------------------#
#Os dados serão enviados para a view Login_create via POST
def login_create(request):
    if not request.POST:
        raise Http404()
    form = LoginForm(request.POST)
    
    if form.is_valid():
        authenticated_user = authenticate(
            username = form.cleaned_data.get('username', ''),
            password = form.cleaned_data.get('password', ''),
        )
        #Sendo o form válido:
        if authenticated_user is not None:
            #messages.success(request, 'Você está logado')
            login(request, authenticated_user)
            
            # Verificar se o usuário pertence a um dos grupos e está cadastrado em alguma sala
            if request.user.groups.filter(name__in=['group_Medicos', 'group_Enfermagem']).exists():
                salas_do_usuario = Salas_Atendimento.objects.filter(profissionalSaude=request.user)
                if not salas_do_usuario.exists():
                    # Usuário não cadastrado em nenhuma sala, redirecionar para a página de criação de sala
                    return redirect('Medicos:salasProfissionalCreate')
                
            return redirect('Atendimento:pagina-inicial')
            
        else:
            messages.error(request, 'Crendenciais inválidas')
            return redirect(reverse('Access_Login:access_login_page'))
    
    #Se o form não for válido:
    else:
        messages.error(request, 'Error ao válidar suas credenciais')    

    return render(request, 'Access_Login/login.html')


#----------------------------END VALIDAÇÃO -----------------------------#  
@login_required(login_url='Access_Login:access_login_page', redirect_field_name='next')
def logout_sme(request):
    if not request.POST:
        return redirect(reverse('Access_Login:access_login_page'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('Access_Login:access_login_page'))

    logout(request)
    return redirect(reverse('Access_Login:access_login_page'))

@login_required(login_url='Access_Login:access_login_page', redirect_field_name='next')
def painel_acesso(request):
    if login:
        messages.success(request, 'Você está logado')         
    return render(request, 'Access_Login:access_login_page')






