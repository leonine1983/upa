from Triagem.models import Atendimento_especializado
from django.views.generic import ListView
from Triagem.models import triagem


class Atend_especializado_LIstView (ListView):
    model = Atendimento_especializado
    template_name = 'Triagem/atend_especializado_listView.html'