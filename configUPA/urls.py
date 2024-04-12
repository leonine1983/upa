from django.urls import path
from .views import upload_video, letreiroCreateView, Create_notifica, Detail_notifica

app_name = 'configUPA'

urlpatterns = [
    path('parametros/upload-background-painel/', upload_video, name='upload_video_painel'),
    path('parametros/letreiro/edit', letreiroCreateView.as_view(), name='letreiroCreate'),
    path('notificacoes_sistema/<int:pk>', Detail_notifica.as_view(), name='notifica'),
    path('create_notificacoes_sistema/', Create_notifica.as_view(), name='notifica_create'),
]
