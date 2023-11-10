from django.urls import reverse
from django.http import Http404
from django.shortcuts import render, redirect
from forms.login import LoginForm
#Para fazer a autenticação vamos importar as seguintes bibliotecas
from django.contrib.auth import authenticate, login
from django.contrib import messages
from Medicos.models import Salas_Atendimento


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
                
            return redirect('Atendimento:lista-paciente')
            
        else:
            messages.error(request, ' ATENÇÃO ⚠️!!! \
            Antes que você conseguisse efetuar o login, detectamos uma tentativa de acesso com senha ou usuário incorretos.... Fique tranquilo(a), o sistema está totalmente seguro. 🚫🔒')
            return redirect(reverse('Access_Login:access_login_page'))
    
    #Se o form não for válido:
    else:
        messages.error(request, 'Error ao válidar suas credenciais')    

    return render(request, 'Access_Login/sign-in/index.html')
