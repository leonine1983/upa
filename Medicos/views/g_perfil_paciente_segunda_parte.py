from django.contrib.auth.decorators import login_required
from django.shortcuts import  render
from Triagem.models import triagem
from Atendimento.models import *
from Medicos.models import Medico_atendimento


# -------------------Cria perfil completo de paciente SEGUNDA PARTE ------------------------------------
@login_required
def paciente_perfil_completo_segunda_parte(request, pk):

    #faço uma busca no model triagem
    dados = triagem.objects.filter(id = pk)
    for d in dados:
        paciente_triagem = d.paciente_triagem_id
        pkk = d.id
        PA = d.pressao_arterial_PA
        FC = d.frequencia_cardiaca_FC
        FR = d.frequencia_respiratoria_FR
        SPO2 = d.saturacao_de_oxigenio_SPO2
        HGT = d.hemoglicoteste_HGT
        TEMP = d.temperatura_TEMP
        peso = d.peso
        observacao = d.observacao
        enfermeira = d.nome_da_enfermeira
    
    dados = envio_triagem.objects.filter(id = paciente_triagem)
    for d in dados:
        paciente = d.paciente_envio_triagem_id

    #Dados contem o id do paciente
    dados = ficha_de_atendimento.objects.filter(id = paciente)
    for d in dados:
        paciente_id = d.id
        paciente_nome = d.nome_social
        paciente_sexo = d.sexo.id
        paciente_sexo_str = d.sexo
        paciente_idade = d.idade
        paciente_nascimento = d.data_nascimento
        paciente_rg = d.RG
        paciente_cpf = d.CPF
        paciente_nacio = d.nacionalidade
        paciente_rua = d.rua
        paciente_bairro = d.bairro
        paciente_cidade = d.cidade
        paciente_estado = d.estado
        paciente_cep = d.CEP
        paciente_mae = d.nome_mae
        paciente_resp = d.responsavel
        paciente_tel = d.tel
        paciente_data_cadast = d.data_cadastro
        paciente_horari_cadast = d.horario_cadastro
        paciente_sus = d.cartao_sus          

    link_envio_triagem = envio_triagem.objects.select_related('paciente_envio_triagem').filter(paciente_envio_triagem_id=paciente)
    link_triagem = pkk    
    link_medico = Medico_atendimento.objects.select_related('paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem').filter(paciente_medico_atendimento__paciente_triagem__paciente_envio_triagem_id=paciente)   
        
    return render(request, 'Medicos/perfis/perfil-paciente_completo_segunda_parte.html', {
        #Dados da ficha do paciente
        'paciente' : dados,
        'paciente_nome': paciente_nome,
        'paciente_sexo' : paciente_sexo,
        'paciente_sexo_str' : paciente_sexo_str,
        'paciente_idade' : paciente_idade,
        'paciente_nascimento' : paciente_nascimento,
        'paciente_rg' : paciente_rg,
        'paciente_cpf' : paciente_cpf,
        'paciente_nacio' : paciente_nacio,
        'paciente_rua' : paciente_rua,
        'paciente_bairro' : paciente_bairro,
        'paciente_cidade' : paciente_cidade,
        'paciente_estado' : paciente_estado,
        'paciente_cep' : paciente_cep,
        'paciente_mae' : paciente_mae,
        'paciente_resp' : paciente_resp,
        'paciente_tel' : paciente_tel,
        'paciente_data_cadast' : paciente_data_cadast,
        'paciente_horari_cadast' : paciente_horari_cadast,
        'paciente_sus' : paciente_sus,
        'link_triagem' : link_triagem,        
        'link_envio_triagem' : link_envio_triagem,
        'link_medico' : link_medico,
        #dadoso da triagem
        'PA'  : PA,
        'FC' : FC,
        'FR' : FR,
        'SPO2'  : SPO2,
        'HGT' : HGT,
        'TEMP' : TEMP,
        'peso' : peso,
        'enfermeira' : enfermeira,
        'observacao' : observacao,
        #fim Triagem
        'pkK': pkk 
        #'lista': envio_triagem_id
    })
    