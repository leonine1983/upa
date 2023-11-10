#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.views.generic.edit import CreateView
from Triagem.models import triagem
from Triagem.forms import TriagemEnfermariaForm
from datetime import date
from django.db.models import Q



# Cadastra somente o id do paciente na TRIAGEM
class triagem_enfermaria(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = triagem
    form_class = TriagemEnfermariaForm
    template_name = 'Triagem/triagem.html'    
    success_message = "Início do atendimento ao paciente! 👩‍⚕️✨"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['paciente_na_triagem'] = triagem.objects.exclude(paciente_triagem__triagem_concluida=1)        
        context ['paciente_na_triagem_concluidos'] = triagem.objects.filter(Q(paciente_triagem__data_triagem_concluida=date.today()) & Q(paciente_triagem__triagem_concluida=1))
        context ['conteudo'] = 'paciente_na_triagem'

        return context
        

    def get_success_url(self):
        obj_ultimo = triagem.objects.latest('pk').id
        obj_EnvioTriagem = triagem.objects.filter(pk=obj_ultimo)

        for pk in obj_EnvioTriagem:
            id = pk.id
            id = int(id)            
        
        # Envia o ID criado do paciente para a view 'triagem_enfermariaUpdate'
        return reverse('Triagem:triagem-enfermaria-update', kwargs={'pk':id})
    