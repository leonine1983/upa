
from django.urls import path

from Access_Login import views

app_name = 'Access_Login'


urlpatterns = [    
    path('', views.access_login, name='access_login_page'),
    path('login/create', views.login_create, name='login_create'),
    path('login/logout', views.logout_sme, name='logout_upa')
]
