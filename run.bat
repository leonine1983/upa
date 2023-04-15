@echo off     
cd /d "C:\site\upa\venv\Scripts"   
call activate.bat     
cd /d "C:\site\upa\"   
py manage.py runserver    
pause    
