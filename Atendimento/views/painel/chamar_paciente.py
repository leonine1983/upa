from Medicos.models import Chamar_P_para_atendimento
from Medicos.models import Chamar_P_para_atendimento
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Salas_Atendimento
from gtts import gTTS
import io
import base64
from django.http import JsonResponse
from Medicos.models import Chamar_P_para_atendimento, Salas_Atendimento, CadastroSala


def chamar_paciente(request):    
    
    # Busca o id do profissional de saúde na primeira chamada de atendimento
    nome_paciente = Chamar_P_para_atendimento.objects.first().nome_paciente
    profissional_id = Chamar_P_para_atendimento.objects.first().profissionalSaude_id 
    sala_do_usuario = Salas_Atendimento.objects.get(profissionalSaude=profissional_id).nomeSala

    nome_paciente_nome = Chamar_P_para_atendimento.objects.first().nome_paciente.paciente_triagem.paciente_envio_triagem.nome_social
    nome_paciente = f'Paciente {nome_paciente}  por favor se dirigir à {sala_do_usuario}'

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

    # Montar a resposta JSON
    print(f'nome do paciente {nome_sala}')

    response_data = {
        'nome_paciente': nome_paciente_nome,
        'nome_paciente2': nome_paciente_nome,
        'nome_sala': nome_sala,
        'audio_base64': audio_base64,    
    }
    return JsonResponse(response_data)
"""
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from gtts import gTTS
import io
import base64

def chamar_paciente(request):
    try:
        # Use get_object_or_404 para garantir que o objeto exista
        chamada_atendimento = get_object_or_404(Chamar_P_para_atendimento)

        nome_paciente = chamada_atendimento.nome_paciente
        profissional_id = chamada_atendimento.profissionalSaude_id
        sala_do_usuario = Salas_Atendimento.objects.get(profissionalSaude=profissional_id).nomeSala

        nome_paciente_msg = f'Paciente {nome_paciente} por favor se dirigir à {sala_do_usuario}'

        # Gerar o áudio em memória
        tts = gTTS(text=nome_paciente_msg, lang='pt-br')
        audio_file = io.BytesIO()
        tts.write_to_fp(audio_file)
        audio_file.seek(0)

        # Ler os dados do áudio em memória e codificá-los em base64
        audio_content = audio_file.read()
        audio_base64 = base64.b64encode(audio_content).decode('utf-8')

        # Certifique-se de que todos os dados são serializáveis
        #triagem_data = chamada_atendimento.triagem.to_json() if chamada_atendimento.triagem else None

        print(f'o nome do usuario {nome_paciente}')

        # Montar a resposta JSON
        response_data = {
            'nome_paciente': nome_paciente,
            #'audio_base64': audio_base64,
            #'triagem_data': triagem_data,
        }
        return JsonResponse(response_data)

    except Exception as e:
        # Lidar com exceções, como se o modelo não existir
        return JsonResponse({'error': str(e)})

"""