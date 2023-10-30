from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from Atendimento.models import envio_triagem


class delete_paciente_a_triagem(LoginRequiredMixin, DeleteView):
    model = envio_triagem
    template_name = 'Atendimento/delete_fila_triagem.html'    
    success_url = reverse_lazy('Atendimento:lista_de_paciente_na_triagem')