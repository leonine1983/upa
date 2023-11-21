@echo off
setlocal enabledelayedexpansion

rem Obter o nome do usuário
set "nome_do_usuario=%USERNAME%"

rem Construir o caminho para a pasta upa
set "caminho_upa=C:\Users\!nome_do_usuario!\AppData\Local\site\upa"

cd %caminho_upa%

echo Ativando o ambiente virtual...
call venv\Scripts\activate

echo Iniciando o servidor Django...
python manage.py runserver 0.0.0.0:80

echo Pressione qualquer tecla para fechar...
pause >nul
