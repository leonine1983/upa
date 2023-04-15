from django.urls import path
from . import views
from .views import triagem_enfermaria, Classifica_risco_view, Classifica_risco_lista_view, Classifica_risco_Update_view


app_name = 'Triagem'

urlpatterns = [
    path('', triagem_enfermaria.as_view(), name='triagem-enfermaria'),
    path('triagem_concluida/<int:pk>', views.triagem_concluida_Update.as_view(), name='triagem_concluida'),
    path('chamar_paciente/<int:pk>/', views.chamar_paciente_triagem, name='chamar_paciente'),
    # Classifica risco
    path('classifica-risco', Classifica_risco_view.as_view(), name='classifica-risco'),
    path('classifica-risco/lista', Classifica_risco_lista_view.as_view(), name='classifica-risco-lista'),   
    path('classifica-risco/update/<int:pk>', Classifica_risco_Update_view.as_view(), name='classifica-risco-Update'),   
    path('triagem/chamar_paciente', views.sua_view, name='chamar_paciente_triagem' ),   
    # cadastro de Enfermeras e Tec-enfermagem
    path('triagem/Enfermerios_e_Tec', views.Enferm_SignUpForm, name='user_create'),
    path('triagem/Enfermeros_e_Tec/atualiza/<int:pk>', views.EnfermUpdateView.as_view(), name='user_atualiza'),
    path('triagem/Enfermeros_e_Tec/deleta/<int:pk>', views.DeleteUserDelet.as_view(), name='user_delete'),
   
]
