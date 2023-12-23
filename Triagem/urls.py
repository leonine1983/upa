from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import triagem_enfermaria, Classifica_risco_view, Classifica_risco_lista_view, Classifica_risco_Update_view, triagem_enfermariaUpdate, triagem_enfermaria_Alergia_Update, triagem_classifica_Risco_update, Triagem_Delete


app_name = 'Triagem'

urlpatterns = [
    path('', triagem_enfermaria.as_view(), name='triagem-enfermaria'),
    path('<int:pk>', triagem_enfermariaUpdate.as_view(), name='triagem-enfermaria-update'),    
    path(
    'alergias/<int:pk>/<str:hora>/<str:data>/<int:paciente_envio_triagem_id>/', 
    triagem_enfermaria_Alergia_Update.as_view(), 
    name='triagem-enfermaria-alergia-update'
),


    
    path('classifica_risco/<int:pk>', triagem_classifica_Risco_update.as_view(), name='triagem_classifica_Risco_update'),
    path('etiqueta/<int:pk>', views.EtiquetaView.as_view(), name='triagem_Etiqueta'),    
    # Atendimento especializado
    path('atend_especializado/', views.Atend_especializado_Create.as_view(), name='triagem_especializada'),    
    path('atend_especializado/List', views.Atend_especializado_LIstView.as_view(), name='triagem_especializada_ListView'),    
    path('atend_especializado/retorno/<int:pk>', views.Atend_especializado_UpdateView.as_view(), name='triagem_especializada_UpdateView'),
    path('triagem_concluida/<int:pk>', views.triagem_concluida_Update.as_view(), name='triagem_concluida'),
    path('triagem/delete/<int:pk>', Triagem_Delete.as_view(), name='triagem-delete'),


    # Classifica risco
    path('classifica-risco', Classifica_risco_view.as_view(), name='classifica-risco'),
    path('classifica-risco/lista', Classifica_risco_lista_view.as_view(), name='classifica-risco-lista'),   
    path('classifica-risco/update/<int:pk>', Classifica_risco_Update_view.as_view(), name='classifica-risco-Update'),   
    # cadastro de Enfermeras e Tec-enfermagem
    path('triagem/Enfermerios_e_Tec', views.Enferm_SignUpForm, name='user_create'),
    path('triagem/Enfermeros_e_Tec/atualiza/<int:pk>', views.EnfermUpdateView.as_view(), name='user_atualiza'),
    path('triagem/Enfermeros_e_Tec/deleta/<int:pk>', views.DeleteUserDelet.as_view(), name='user_delete'),
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
