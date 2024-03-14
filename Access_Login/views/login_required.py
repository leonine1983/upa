from django.urls import reverse
from django.shortcuts import render, redirect
#Para fazer a autenticação vamos importar as seguintes bibliotecas
from django.contrib.auth import login, logout
from django.contrib import messages
from Medicos.models import Salas_Atendimento
from django.contrib.auth.models import User
#Para impedir que acessem as paginas sem está logado usamos LOGIN_REQUIRED
from django.contrib.auth.decorators import login_required
import threading
import time

@login_required(login_url='Access_Login:access_login_page', redirect_field_name='next')
def logout_sme(request):
    

    try:
        profissional = Salas_Atendimento.objects.get(profissionalSaude = request.user.id)
        profissional.delete()

        def do_logout():
            time.sleep(1)
            logout(request)
        
        # Criar uma thread para fazer logout após 30 segundos
        logout_thread = threading.Thread(target=do_logout)
        logout_thread.start()
    except:
        def do_logout():
            time.sleep(1)
            logout(request)
        
        # Criar uma thread para fazer logout após 30 segundos
        logout_thread = threading.Thread(target=do_logout)
        logout_thread.start()
    
    return redirect(reverse('Access_Login:access_login_page'))
    

@login_required(login_url='Access_Login:access_login_page', redirect_field_name='next')
def painel_acesso(request):
    if login:
        messages.success(request, 'Você está logado')         
    return render(request, 'Access_Login:access_login_page')






