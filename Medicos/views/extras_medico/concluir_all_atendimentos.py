from Medicos.models import Medico_atendimento
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from datetime import date

def conclui_all(request):
    # Filtrando os objetos Medico_atendimento onde final_medico_atendimento é diferente de '1'
    atend_all = Medico_atendimento.objects.exclude(paciente_medico_atendimento__final_medico_atendimento='1')
    atend = atend_all.exclude(data_medico = date.today())

    # Verifica se há objetos encontrados
    if atend:
        # Itera sobre os objetos encontrados
        for at in atend:
            # Define o campo final_medico_atendimento como '1'
            at.paciente_medico_atendimento.final_medico_atendimento = '1'
            # Salva as alterações no objeto triagem
            at.paciente_medico_atendimento.save()
            messages.success(request, "Registros de atendimento ao paciente foram concluídos com êxito!")
    return redirect(reverse_lazy('Medicos:medico_prontuario'))


"""

from .models import Licenca
from django.contrib.auth.models import User
from django.utils import timezone

# Atividade da lincença
def licenca_context(request):
    licenca_ativa = Licenca.objects.filter(ativa=True, expiracao__gt=timezone.now()).first()
    name_sistem = "SG-UPA"
    
    if licenca_ativa is None:
        # Obtem todos os superusuários
        superusers = User.objects.filter(is_superuser=True)
        users = User.objects.exclude(is_superuser=True)
        # Percorrer todos os usuários superusuários e desativando-os

        for user in users:
            user.is_active = False
            user.save()
        
        for superuser in superusers:
            superuser.is_active = True
            superuser.save()
    else:
        # Caso exista uma licença ativa, definir todos os usuários como ativos
        User.objects.update(is_active=True)

    
    return {'licenca_ativa': licenca_ativa, 'name_sistem':name_sistem}

# Atividade da lincença

"""