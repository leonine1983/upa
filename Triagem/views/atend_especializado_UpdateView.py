from Triagem.models import Atendimento_especializado
from django.views.generic import UpdateView
from .atend_especializado_UpdateView_Form import *
from Triagem.models import triagem
from django.urls import reverse_lazy


class Atend_especializado_UpdateView(UpdateView):
    model = Atendimento_especializado
    #fields = ['tipo_atendimento', 'descreve_solicitacao', 'pk_paciente']
    form_class = Atend_especializado_UpdateView_Form
    template_name = 'Triagem/atend_especializado_listView.html'
    success_url = reverse_lazy('Medicos:medico_prontuario')

    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        pk = self.kwargs['pk'] 
        contexto['pk'] = pk
        contexto['page'] = "retorno"
        contexto['object_list'] = Atendimento_especializado.objects.filter(id = pk)

        return contexto