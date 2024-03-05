from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from Atendimento.models import envio_triagem
from datetime import timedelta
 

#cria a lista
@login_required
def lista_de_paciente_na_triagem(request):
    
    start_date = request.GET.get('start_date')
    date_today = datetime.today()
    #converte o formato da data
    date_hoje = '{}-{}-{}'.format(date_today.year, date_today.month, date_today.day)
    
    if start_date:
        #converte a str objects em date
        date = datetime.strptime(start_date, '%Y-%m-%d')        
        
        #converte o formato da data
        date_format = '{}-{}-{}'.format(date.year, date.month, date.day)

        object_list = envio_triagem.objects.all()
       
        #formata o mês por extenso
        #mes_extenso = {1:'Janeiro', 2:'Fevereiro', 3:'Março', 4:'Abril', 5:'Maio', 6:'Junho', 7:'Julho', 8:'Agosto', 9:'Setembro', 10:'Outubro', 11:'Novembro', 12:'Dezembro'}    
        #mes = mes_extenso[date.month]
        #data = f"{date.day} de {mes} de {date.year}"
        #object_list = envio_triagem.objects.all()
        print(date_format)  
        
        if date_format:
            object_list = envio_triagem.objects.filter(data_envio_triagem = date_format) 
        else:             
            object_list = envio_triagem.objects.all() & envio_triagem.objects.exclude(triagem_concluida = 1)
    else:
        object_list = envio_triagem.objects.filter(data_envio_triagem = date_hoje) & envio_triagem.objects.exclude(triagem_concluida = 1)
        #object_list = envio_triagem.objects.all()
        #print(f'a data de hoje e {date_hoje}')

    pacientes_em_menos_de_48_horas = []
    
    for triagem in object_list:
        diferenca_tempo = datetime.now() - datetime.combine(triagem.data_envio_triagem, triagem.horario_triagem)
        if diferenca_tempo < timedelta(hours=48):
            triagem.retornou_em_menos_de_48_horas = True
            triagem.save()
            pacientes_em_menos_de_48_horas.append(triagem)

    data_hoje = datetime.today()    

    return render(request, 'Atendimento/envio_a_triagem.html', {
        'lista_db' : object_list,
        'data_hoje' : date_hoje,
        'url' :   'Atendimento:envio_paciente_a_triagem',  
    })

