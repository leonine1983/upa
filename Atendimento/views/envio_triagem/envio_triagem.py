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
from Triagem.models import triagem



class envio_paciente_a_triagem(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = envio_triagem
    fields = ['paciente_envio_triagem', 'nome_acompanhante']   
    #form_class = Envio_Form
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')
    success_message = "Paciente enviado com sucesso para a fila de classificação! 🚀"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context ['envio_triagem'] = 'on'
        return context
    
    
    def form_valid(self, form):
        paciente = form.cleaned_data['paciente_envio_triagem']

        ultima_triagem = envio_triagem.objects.filter(
            paciente_envio_triagem=paciente
        )

        if ultima_triagem.exists():
            ultima_triagem_obj = ultima_triagem.order_by('-data_envio_triagem', '-horario_triagem').first()
            data = ultima_triagem_obj.data_envio_triagem
            hoje = datetime.today().date()
            diferenca = (hoje - data).days

            if diferenca < 4:
                form.instance.horas48 = True
                mensagem = mark_safe(f'<i class="fa-thin fa-skull-crossbones"></i> Paciente {paciente.nome_social} atendido em menos de 48 horas. Tratar como maior urgência.')
                messages.warning(self.request, mensagem, extra_tags='alert-warning')
            else:
                form.instance.horas48 = False

        # Adicione um print para depuração
        print(f'Valor do campo antes de salvar: {form.instance.horas48}')

        # Salve o paciente
        form.save()

        # Adicione um print para depuração
        print(f'Valor do campo após salvar: {form.instance.horas48}')

        return super().form_valid(form)
