
from django.contrib import admin
from django.urls import path, include
from django.urls import path, re_path
from configUPA.views import handler404, handler500


urlpatterns = [
    path('admin/', admin.site.urls),
    #Django_select2
    #Atendimento de emergencia
    path('', include('Access_Login.urls')),
    path('atendimento/', include('Atendimento.urls')),
    path('triagem/', include('Triagem.urls')),
    path('medicos/', include('Medicos.urls')),
    path('configura/', include('configUPA.urls')),
    path('imprime/', include('PrintPDFs.urls')),
    re_path(r'^.*/$', handler404),
    re_path(r'^.*/500/$', handler500),
]

