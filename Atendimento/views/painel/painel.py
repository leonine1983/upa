
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from configUPA.models import config_Marquee, Video_Backgroud_Painel
#cria o painel para chamar os pacientes
from django.shortcuts import render
from datetime import datetime
from configUPA.models import config_Marquee


# View para gerar o áudio e renderizar o template com o áudio em base64
def painel(request):    
    # Enviar o áudio como contexto para o template
    configUpa = config_Marquee.objects.all()    
    video_obj = Video_Backgroud_Painel.objects.first().video_file

    if video_obj:
        video = video_obj.video_file
    else:
        video = "video"


    return render(request, 'Atendimento/painel_pacientes/painel.html', {
        'now': datetime.now(),
        'configUpa': configUpa,
        'videoUpa': video})