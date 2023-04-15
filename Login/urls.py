from django.urls import path
from Login import views

namespace='Login'

urlpatterns = [
    path('', views.login, name='acesso_login')
]
