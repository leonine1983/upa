
from django.urls import path

from Access_Login import views

app_name = 'Access_Login'


urlpatterns = [    

    path('', views.access_login, name='access_login_page'),
    path('login/create', views.login_create, name='login_create'),
    #path('painel_acesso/', views.painel_acesso, name='painel_acesso'),
    #url para o logout
    path('login/logout', views.logout_sme, name='logout_upa')


    #path('login/', views.login_view, name='login'),
    #path('profile/', views.profile_view, name='profile'),
    

]
