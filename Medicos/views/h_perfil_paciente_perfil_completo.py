from django.contrib.auth.decorators import login_required
from django.shortcuts import  render
from django.shortcuts import render
from Triagem.models import triagem
from Atendimento.models import *
from django.contrib.auth.hashers import make_password


# Essa view replicam o perfil do paciente, e do link visivel aos medicos
# e recebem o id a partir da ficha de atendimento ao inves de triagem
@login_required
def paciente_perfil_completo_menu_lateral(request, pk):
    dados = envio_triagem.objects.filter(paciente_envio_triagem_id=pk)
    if dados.exists():
        for d in dados:
            dados = triagem.objects.filter(paciente_triagem_id = d.id)
            for d in dados:
                pkk = d.id
                data_t = d.data_triagem
    else:
        pkk = 0 
        data_t = 0    
    paciente = pk

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
  
    return render(request, 'Medicos/perfis/perfil-paciente_completo.html', {
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
        'pkK': pkk, 
        'data_t' : data_t
        #'lista': envio_triagem_id
    }) 
    