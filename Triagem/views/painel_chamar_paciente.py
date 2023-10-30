
from django.shortcuts import render
from django.http import JsonResponse
from Triagem.models import ChamarPaciente     

    
def sua_view(request):
  if request.method == 'POST':
    id_paciente = request.POST['paciente_id']
    nome_paciente = request.POST['nome_paciente']
    novo_chamado = ChamarPaciente(id_paciente=id_paciente, nome_paciente=nome_paciente)
    novo_chamado.save()
    return JsonResponse({'status': 'ok'})
  return render(request, 'sua_template.html')