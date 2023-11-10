from django.urls import reverse
from django.shortcuts import render
from forms.login import LoginForm
#Para fazer a autenticação vamos importar as seguintes bibliotecas
from django.contrib.auth import logout
from django.contrib import messages


# Create your views here.
def access_login(request):
    form = LoginForm()
    if logout:
        messages.success(request, f'Parabéns! Você efetuou o login no sistema com sucesso! 🎉')


    return render(request, 'Access_Login/sign-in/index.html',  {
        'form' : form,
        'form_action' : reverse('Access_Login:login_create')
    })
    