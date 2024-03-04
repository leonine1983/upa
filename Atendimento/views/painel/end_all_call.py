from django.shortcuts import redirect
from Medicos.models import Chamar_P_para_atendimento
from django.contrib.auth.decorators import login_required

@login_required
def del_all_call(request):
    Chamar_P_para_atendimento.objects.all().delete()
    return redirect('Atendimento:lista-paciente')
