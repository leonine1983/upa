# Sistema-de-Gerenciamento-de-UPA

Sistema-de-Gerenciamento-de-UPA---Unidade-de-Pronto-Atendimento
Projeto em DESENVOLVIMENTO para atender às necessidades administrativas das unidades de pronto atendimento.

Este sistema está sendo "desenhado" à medida da unidade de pronto atendimento do município de Vera Cruz, no entanto, suas características estruturais permite que esse sistema possa ser implantado em outras unidades de pronto de atendimento de outros municípios.

C:\Users\<seu_usuario>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup


------------------------------------------------------------------------
------------------------------------------------------------------------
Aqui está a versão atualizada do script para fazer PULL automaticamente
------------------------------------------------------------------------
------------------------------------------------------------------------

# Obtém o nome do usuário
$nome_do_usuario = $env:USERNAME

# Constrói o caminho para o diretório do repositório Git
$caminho_upa = "C:\Users\$nome_do_usuario\AppData\Local\site\upa"

# Muda para o diretório do repositório
cd $caminho_upa

# Nome da branch principal
$branch_principal = "main"

# Obtém o status da branch principal
$status = git status -b

# Verifica se há mudanças a serem puxadas
if ($status -contains "Your branch is behind") {
    # Executa o comando git pull para obter as mudanças do repositório remoto
    git pull origin $branch_principal
    Write-Host "Mudanças foram puxadas da branch $branch_principal do repositório remoto."
} else {
    Write-Host "Não há mudanças a serem puxadas na branch $branch_principal."
}

------------------------------------------------------------------------
------------------------------------------------------------------------
Neste script, a variável $branch_principal é usada para armazenar o nome da branch principal (no seu caso, "main"). O comando git pull origin $branch_principal realiza o pull das mudanças da branch principal do repositório remoto.

Salve o script e execute-o da mesma forma no PowerShell:
.\check_and_pull.ps1


------------------------------------------------------------------------
------------------------------------------------------------------------
Crie o Script PowerShell:

Use o script PowerShell fornecido anteriormente e salve-o com uma extensão .ps1, por exemplo, check_and_pull.ps1.
Abra o Agendador de Tarefas:

Pressione Win + R para abrir a caixa de diálogo Executar.
Digite taskschd.msc e pressione Enter para abrir o Agendador de Tarefas do Windows.
Crie uma Nova Tarefa:

No Agendador de Tarefas, clique com o botão direito em "Biblioteca do Agendador de Tarefas" no painel esquerdo.
Escolha "Criar Tarefa Básica".
Siga o Assistente:

No assistente, dê um nome à sua tarefa e uma descrição (opcional).
Selecione "Iniciar o Programa" e clique em Avançar.
Configure o Programa a ser Executado:

Navegue até o local do seu script PowerShell usando o botão "Procurar...". Selecione o script check_and_pull.ps1.
Clique em Avançar.
Configure o Agendamento:

Escolha "Diariamente" ou "Semanalmente", dependendo da frequência desejada.
Defina a hora específica que você deseja que o script seja executado automaticamente.
Clique em Avançar.
Revisão e Conclusão:

Revise as configurações e clique em Concluir.

------------------------------------------------------------------------
------------------------------------------------------------------------

