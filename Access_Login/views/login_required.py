from django.urls import reverse
from django.shortcuts import render, redirect
#Para fazer a autenticação vamos importar as seguintes bibliotecas
from django.contrib.auth import login, logout
from django.contrib import messages
#Para impedir que acessem as paginas sem está logado usamos LOGIN_REQUIRED
from django.contrib.auth.decorators import login_required


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






