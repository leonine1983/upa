#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView
from Triagem.models import triagem


#Cria etiqueta
class EtiquetaView(LoginRequiredMixin, TemplateView):
    template_name = 'Triagem/etiqueta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')  # Obtém o valor do parâmetro 'pk' da URL
        paciente = triagem.objects.filter(paciente_triagem_id = pk)        
        for pac in paciente:
            nome = pac.paciente_triagem.paciente_envio_triagem.nome_social
            idade = pac.paciente_triagem.paciente_envio_triagem.idade
            d_nas = pac.paciente_triagem.paciente_envio_triagem.data_nascimento
            clas_tipo = pac.classifica_tipo
        context['nome_paciente'] = nome    
        context['idade'] = idade    
        context['horario_entrada'] = d_nas
        context['classificacao_risco'] = clas_tipo
        context['pk'] = pk
        
        return context
        