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
    nome_paciente_2 = Chamar_P_para_atendimento.objects.first().nome_paciente
    profissional_id = Chamar_P_para_atendimento.objects.first().profissionalSaude_id  
    print(f'id do profissional {profissional_id}')     
    # Busca o objeto Salas_Atendimento que corresponde ao profissional de saúde encontrado
    sala_do_usuario = Salas_Atendimento.objects.get(profissionalSaude=profissional_id).nomeSala
    print(f'id da sala: {sala_do_usuario}')
    # Busca o nome da sala correspondente no modelo CadastroSala
    #nome_sala = CadastroSala.objects.get(id=sala_do_usuario.nomeSala_id).nome_Sala        
    print(f'nome da sala {sala_do_usuario}')

    nome_paciente = f'Paciente {nome_paciente}  por favor se dirigir à {sala_do_usuario}'
    print(f'essa e a data {Chamar_P_para_atendimento.objects.first().data_chamada}') 
    
    # Gerar o áudio em memória
    tts = gTTS(text=nome_paciente, lang='pt-br')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    # Ler os dados do áudio em memória e codificá-los em base64
    audio_content = audio_file.read()
    audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    # Montar a resposta JSON
    response_data = {
        #'nome_paciente': nome_paciente,
        #'nome_sala': nome_sala,
        #'data_chamada': Chamar_P_para_atendimento.objects.first().data_chamada,
        #'nome_paciente2': nome_paciente_2,
        #'data_criacao': Chamar_P_para_atendimento.objects.first().data_criacao,
        #'data_atualizacao': Chamar_P_para_atendimento.objects.first().data_atualizacao,
        'audio_base64': audio_base64,    
    }
    return JsonResponse(response_data)
