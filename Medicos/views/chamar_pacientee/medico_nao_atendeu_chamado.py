
from Triagem.models import triagem
from Medicos.models import Chamar_P_para_atendimento, Medico_atendimento, CustomUser
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse

def medico_paciente_nao_atende (request, pk):
     # Verificar se o paciente existe
     paciente_triagem = get_object_or_404(triagem, pk = pk)    
     medico = CustomUser.objects.filter(user_id = request.user.id)
     if medico:
        for m in medico:
            medico_nome =f'{m.user.first_name} {m.user.last_name} | CRM n° {m.crm}'
     else:
         medico_nome = request.user.username
        
     paciente_triagem.nome_medico_respondeu_ao_chamado = medico_nome
     print(f'o nome do medico e {medico_nome}')
     

     # Informar que o paciente não respondeu ao chamado
     paciente_triagem.medico_respondeu_ao_chamado = True

     # Indica a quantidade de chamadas para o paciente
     paciente_triagem.medico_chamadas_contabilizadas += 1

     # Salvar
     paciente_triagem.save()
     messages.info(request, "O paciente não respondeu ao chamado")

     # Exclui os registros de chamado do paciente ativo
     Chamar_P_para_atendimento.objects.filter(nome_paciente=paciente_triagem).delete()

     return redirect(reverse("Medicos:medico_prontuario"))

    