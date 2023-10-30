from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem, ficha_de_atendimento


#criar a pagina de cadastro
class envio_paciente_a_triagem_2(LoginRequiredMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']      
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context ['get_id'] = ficha_de_atendimento.objects.filter(id = self.kwargs['pk']) 
        return context
    
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')