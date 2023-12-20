from django.shortcuts import redirect
from django.contrib import messages

from Medicos.models import Chamar_P_para_atendimento

def Update_chama_usuario_pos_atendimento(request, pk):
    instance = Chamar_P_para_atendimento.objects.get(pk=pk)
    instance.chamado = True
    instance.save()
    pk_p = Chamar_P_para_atendimento.objects.filter(pk=pk)
    for p in pk_p:
        pk_id = p.nome_paciente.id

    messages.error(request, "Chamada de paciente cancelada com êxito! 🚫✅")
    messages.success(request, "Atendimento concluído com sucesso! ✅")
        
        
    return redirect('Medicos:dados_do_paciente_medicamentos', pk=pk_id)
    #return redirect('Medicos:dados do paciente', kwargs={'pk':pk_id})