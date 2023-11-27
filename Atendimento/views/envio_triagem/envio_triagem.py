from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem 
from datetime import timezone, datetime, timedelta
from django.http import HttpResponseBadRequest
from django.utils.safestring import mark_safe

class envio_paciente_a_triagem(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem']
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





    """
    
    def form_valid(self, form):
        # Verifica se o paciente já foi enviado para triagem nas últimas 48 horas
        paciente = form.cleaned_data['paciente_envio_triagem']
        ultima_triagem = envio_triagem.objects.filter(paciente_envio_triagem=paciente).order_by('-data_envio_triagem', '-horario_triagem').first()

        if ultima_triagem:
            diferenca_tempo = timezone.now() - datetime.combine(ultima_triagem.data_envio_triagem, ultima_triagem.horario_triagem)
            if diferenca_tempo < timedelta(hours=48):
                return HttpResponseBadRequest("Erro: Paciente atendido em menos de 48 horas. Tratar como maior urgência.")

        return super().form_valid(form)
    """