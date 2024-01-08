from django.contrib.auth.decorators import login_required
#bloquear acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView

from Atendimento.models import Bairro



class Bairro_Delete(LoginRequiredMixin, DeleteView): 
    success_message = 'Usuário excluído com sucesso.'
    model = Bairro
    template_name = 'Atendimento/cadastros_genericos/delete.html'
    success_url = reverse_lazy('Atendimento:list_bairro')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        context['object_name'] = obj.__str__()
        context['object_id'] = obj.id
        context['deleta_bairro'] = 'bairro'
        return context
