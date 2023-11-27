from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem, ficha_de_atendimento
from datetime import datetime, timedelta
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


#criar a pagina de cadastro
class envio_paciente_a_triagem_2(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']      
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context ['get_id'] = ficha_de_atendimento.objects.filter(id = self.kwargs['pk']) 
        return context
    
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')
    success_message = "Paciente enviado com sucesso para a fila de classificação! 🚀"

    # Verificar se o usuário foi atendido em menos de 48 horas
    def form_valid(self, form):
        paciente = form.cleaned_data['paciente_envio_triagem']
        ultima_triagem = envio_triagem.objects.filter(paciente_envio_triagem=paciente).order_by('-data_envio_triagem', '-horario_triagem').first()

        if ultima_triagem:
            diferenca_tempo = datetime.now() - datetime.combine(ultima_triagem.data_envio_triagem, ultima_triagem.horario_triagem)
            if diferenca_tempo < timedelta(hours=48):
                # Adicionar ícone à mensagem de aviso como HTML seguro
                nome_paciente = form.cleaned_data['paciente_envio_triagem'].nome_social
                mensagem = mark_safe(f'<i class="fa-thin fa-skull-crossbones"></i> Paciente {nome_paciente} atendido em menos de 48 horas. Tratar como maior urgência.')
                messages.warning(self.request, mensagem, extra_tags='alert-warning')
        return super().form_valid(form)