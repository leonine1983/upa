from Medicos.models import Chamar_P_para_atendimento
from Medicos.models import Chamar_P_para_atendimento
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Salas_Atendimento
from datetime import datetime, timedelta
from gtts import gTTS
import io
import os
from django.conf import settings
import base64
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Salas_Atendimento
from django.core.serializers import serialize
from django.utils.safestring import mark_safe


def chamar_paciente(request):    
    nome_ultimos_chamado = []
    nome_ultimos_chamado_all = ''

    try:
        # Busca o id do profissional de saúde na primeira chamada de atendimento
        nome_paciente = Chamar_P_para_atendimento.objects.filter(chamado=False).first().nome_paciente    

        profissional_id = Chamar_P_para_atendimento.objects.first().profissionalSaude_id 
        sala_do_usuario = Salas_Atendimento.objects.get(profissionalSaude=profissional_id).nomeSala

        nome_paciente_nome = Chamar_P_para_atendimento.objects.first().nome_paciente.paciente_triagem.paciente_envio_triagem.nome_social
        nome_paciente = f'Paciente {nome_paciente}  por favor se dirigir à {sala_do_usuario}'

        data_atual = datetime.now().date()

        # Filtra a queryset para incluir apenas registros do dia atual
        nome_paciente_chamado = Chamar_P_para_atendimento.objects.filter(data_chamada__date=data_atual)[:5]
        nome_paciente_chamado_data = {}
        
        for n in nome_paciente_chamado:
            data_chamada = n.data_chamada
            hora_formato = data_chamada.strftime('%H:%M')
            data_formato = data_chamada.strftime('%d/%m/%Y')  # Definindo data_formato dentro do bloco
            chamado = f"<li class='fs-5'><i class='fa-thin fa-hospital-user'></i> {n.nome_paciente} - <i class='fa-regular fa-clock'></i> {hora_formato} em {data_formato}</li>"
            nome_ultimos_chamado.append(chamado)
            
            nome_ultimos_chamado_all = ''
            for a in nome_ultimos_chamado:                
                nome_ultimos_chamado_all += a
        print(f'{nome_ultimos_chamado_all} paciente chamado')
        
        sala = Salas_Atendimento.objects.filter(profissionalSaude=profissional_id)
        for s in sala:
            nome_sala = s.nomeSala.nome_Sala    
        
        # Gerar o áudio em memória
        tts = gTTS(text=nome_paciente, lang='pt-br')
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        # Ler os dados do áudio em memória e codificá-los em base64
        audio_content = audio_file.read()
        audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    except:
         # Filtra a queryset para incluir apenas registros do dia atual
        data_atual = datetime.now().date()
        nome_paciente_chamado = Chamar_P_para_atendimento.objects.filter(data_chamada__date=data_atual)[:5]
        nome_paciente_chamado_data = {}
        for n in nome_paciente_chamado:
            data_chamada = n.data_chamada
            hora_formato = data_chamada.strftime('%H:%M')
            data_formato = data_chamada.strftime('%d/%m/%Y')  # Definindo data_formato dentro do bloco
            chamado = f"<li class='fs-5'><i class='fa-thin fa-hospital-user'></i> {n.nome_paciente} - <i class='fa-regular fa-clock'></i> {hora_formato} em {data_formato}</li>"
            nome_ultimos_chamado.append(chamado)
            
            for a in nome_ultimos_chamado:
                nome_ultimos_chamado_all += a
            
        nome_paciente_nome = "Atualizando..."
        nome_sala = "Atualizando..."

        audio_file_path = os.path.join(settings.MEDIA_ROOT, 'descanso.mp3')
        # Lê o conteudo do arquivo de audio
        with open(audio_file_path, "rb") as audio_file:
            audio_content = audio_file.read()
        
        # Converter o audio em base64
        audio_base64 = base64.b64encode(audio_content).decode('utf-8')    

    response_data = {
        'nome_paciente_chamado' : mark_safe(nome_ultimos_chamado_all),
        'nome_paciente': nome_paciente_nome,
        'nome_paciente2': nome_paciente_nome,
        'nome_sala': nome_sala,
        'audio_base64': audio_base64,    
    }
    return JsonResponse(response_data)
