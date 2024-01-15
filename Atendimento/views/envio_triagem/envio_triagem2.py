from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Atendimento.models import envio_triagem, ficha_de_atendimento
from datetime import datetime, timedelta, timezone
from django.utils.safestring import mark_safe
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse
from django.shortcuts import redirect
from .envio_form import Envio_Form


#criar a pagina de cadastro
# ...

class envio_paciente_a_triagem_2(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = envio_triagem
    #fields = ['paciente_envio_triagem', 'nome_acompanhante']      
    form_class = Envio_Form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        
        context ['get_id'] = ficha_de_atendimento.objects.filter(id = self.kwargs['pk']) 
        context ['envio_triagem'] = 'on'
        return context
    
    template_name = 'Atendimento/envio_a_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')
    success_message = "Paciente enviado com sucesso para a fila de classificação! 🚀"


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
                
                print(f'Valor da diferença: {diferenca}')

                if diferenca < 2:
                    form.instance.horas48 = True
                    mensagem = mark_safe(f'<i class="fa-thin fa-skull-crossbones"></i> Paciente {paciente.nome_social} atendido em menos de 48 horas. Tratar como maior urgência.')
                    messages.warning(self.request, mensagem, extra_tags='alert-warning')
                else:
                    form.instance.horas48 = False


            # Salve o paciente
            form.save()

            return super().form_valid(form)





