from django.shortcuts import render
from Atendimento.models import envio_triagem


def chamar_paciente_triagem(request, pk):
    data = envio_triagem.objects.filter(pk = pk)   
    return render(request, 'Triagem/chamar_paciente.html',
                  {
        'data_triagem' : data
                  })
                  