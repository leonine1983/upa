from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem , ficha_de_atendimento
from datetime import timezone, datetime, timedelta
from django.utils.safestring import mark_safe
from .envio_form import Envio_Form


class envio_paciente_a_triagem(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = envio_triagem
    #fields = ['paciente_envio_triagem', 'retornou_em_menos_de_48_horas', 'nome_acompanhante']   
    form_class = Envio_Form
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')
    success_message = "Paciente enviado com sucesso para a fila de classificação! 🚀"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context ['envio_triagem'] = 'on'
        return context

    def form_valid(self, form):
        paciente = form.cleaned_data['paciente_envio_triagem']
        paciente.retornou_em_menos_de_48_horas = False  # ou True, conforme a lógica do seu código

        ultima_triagem = envio_triagem.objects.filter(
            paciente_envio_triagem=paciente
        ).order_by('-data_envio_triagem', '-horario_triagem').first()

        print(f'ultima triagem {ultima_triagem}')
        
        if ultima_triagem is not None:
            registros_48_horas = envio_triagem.objects.filter(
                paciente_envio_triagem=paciente,
                data_envio_triagem__gte=datetime.now() - timedelta(hours=48)
            ).exclude(id=ultima_triagem.id if ultima_triagem else None)

            if registros_48_horas.count() > 1:
                paciente.retornou_em_menos_de_48_horas = True

            nome_paciente = form.cleaned_data['paciente_envio_triagem'].nome_social
            mensagem = mark_safe(f'<i class="fa-thin fa-skull-crossbones"></i> Paciente {nome_paciente} atendido em menos de 48 horas. Tratar como maior urgência.')
            messages.warning(self.request, mensagem, extra_tags='alert-warning')

        # Salve o paciente
        paciente.save()

        return super().form_valid(form)

