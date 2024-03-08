from django.shortcuts import redirect, get_object_or_404
from Triagem.models import triagem

def iniciar_atendimento_view(request, pk):
    # Obtém a instância de triagem pelo pk
    instance = get_object_or_404(triagem, pk=pk)
    
    # Define passou_por_atend_medico como True
    instance.passou_por_atend_medico = True
    instance.save()
    
    # Redireciona para a view 'medico_atendimento' com o mesmo pk
    return redirect('Medicos:dados do paciente', pk=pk)
