from django.shortcuts import redirect

from Medicos.models import Chamar_P_para_atendimento

def Update_chama_usuarioo(request, pk):
    instance = Chamar_P_para_atendimento.objects.get(pk=pk)
    instance.chamado = True
    instance.save()
    pk_p = Chamar_P_para_atendimento.objects.filter(pk=pk)
    for p in pk_p:
        pk_id = p.nome_paciente.id
        
    return redirect('Medicos:dados do paciente', pk=pk_id)
    #return redirect('Medicos:dados do paciente', kwargs={'pk':pk_id})