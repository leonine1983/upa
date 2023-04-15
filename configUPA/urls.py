from django.urls import path
from .views import upload_video, letreiroCreateView

app_name = 'configUPA'

urlpatterns = [
    path('parametros/upload-background-painel/', upload_video, name='upload_video_painel'),
    path('parametros/letreiro/edit', letreiroCreateView.as_view(), name='letreiroCreate'),
]
