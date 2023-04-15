from django.urls import include, path

from . import views
from .views import (delete_paciente_a_triagem, envio_paciente_a_triagem,
                    lista_de_paciente_na_triagem, paciente_cadastro,
                    paciente_lista)


app_name='Atendimento'

urlpatterns = [
    #Página Inicial
    path('', views.pagina_inicial, name='pagina-inicial'),   
    path('painel', views.painel, name='painel'), 
    path('painel_atendimento_Medico', views.chamar_paciente, name='chamar_paciente'),
    path('painel_tiragem', views.chamar_paciente, name='chamar_paciente_triagem'),




    path('paciente/listagem', paciente_lista.as_view(), name='lista-paciente'),
    path('paciente/registro', paciente_cadastro.as_view() , name='registro-paciente'),
    path('paciente/registro/<int:pk>', views.paciente_atualizar.as_view() , name='atualizar-paciente'),
    #Perfil do paciente
    path('paciente/perfil/<int:pk>', views.perfil_paciente, name='perfil-paciente'),
    path('paciente/perfil/historico/<int:pk>', views.perfil_paciente_hist, name='perfil-paciente-hist'),
    #FILA DE TRIAGEM    
    path('paciente/envio-paciente', envio_paciente_a_triagem.as_view(), name='envio_paciente_a_triagem'),    
    path('paciente/envio-paciente/<int:pk>', views.envio_paciente_a_triagem_2.as_view(), name='envio_paciente_a_triagem_2'),    
    path('paciente/triagem', views.lista_de_paciente_na_triagem, name='lista_de_paciente_na_triagem'),    
    path('paciente/triagem/<int:pk>', delete_paciente_a_triagem.as_view(), name='delete_de_paciente_na_triagem')

]
