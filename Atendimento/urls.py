from django.urls import include, path

from . import views
from .views import (delete_paciente_a_triagem, envio_paciente_a_triagem,
                    lista_de_paciente_na_triagem, paciente_cadastro,
                    paciente_lista)


app_name='Atendimento'

urlpatterns = [
    #Página Inicial
    path('resumo/', views.pagina_inicial, name='pagina-inicial'), 
    path('paciente/listagem', paciente_lista.as_view(), name='lista-paciente'),


    path('painel', views.painel, name='painel'), 
    path('painel_atendimento_Medico', views.chamar_paciente, name='chamar_paciente'),
    #path('painel_tiragem', views.chamar_paciente, name='chamar_paciente_triagem'),

    # Cadastro Etnia
    path('cadastro/sexo', views.Etnia_CreateView.as_view(), name='cadastra_etnia'),    

    # Cadastro Sexo
    path('cadastro/sexo', views.Sexo_CreateView.as_view(), name='cadastra_sexo'),    

    # Cadastro Pais
    path('cadastro/pais', views.Pais_CreateView.as_view(), name='cadastra_pais'),    

    # Cadastro Estado
    path('cadastro/estado', views.Estado_CreateView.as_view(), name='cadastra_estado'),    


    # Cadastro Cidade
    path('cadastro/cidade', views.Cidade_CreateView.as_view(), name='cadastra_cidade'),    

    # Cadastro Bairro
    path('cadastro/bairro', views.Bairro_CreateView.as_view(), name='cadastra_bairro'),    
    path('bairro/lista', views.Bairro_ListView.as_view(), name='list_bairro'),
    path('bairro/update/<int:pk>', views.Bairro_UpadateView.as_view(), name='Update_bairro'),
    path('bairro/deleta/<int:pk>', views.Bairro_Delete.as_view(), name='delete_bairro'),
    # Cadastro rua
    path('cadastro/Rua', views.Rua_CreateView.as_view(), name='cadastra_rua'),    
    path('Rua/lista', views.Rua_ListView.as_view(), name='list_rua'),
    path('Rua/update/<int:pk>', views.Rua_UpadateView.as_view(), name='Update_rua'),
    path('Rua/deleta/<int:pk>', views.Rua_Delete.as_view(), name='delete_rua'),
    

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
