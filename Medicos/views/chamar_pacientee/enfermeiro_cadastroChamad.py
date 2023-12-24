# views.py
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View
from Medicos.forms import ChamarPacienteForm
from Medicos.models import Chamar_P_para_atendimento, Medico_atendimento
from django.contrib.auth.models import User
from Triagem.models import triagem

class EnfermeiroChamaPacienteView(SuccessMessageMixin, View):
    template_name = 'seu_template.html' 
    success_message = "Paciente chamado com sucesso"

    def post(self, request, pk):
        form = ChamarPacienteForm(request.POST)
        if form.is_valid():
            nome_paciente_id = form.cleaned_data['nome_paciente']
            profissionalSaude_id_username = form.cleaned_data['profissionalSaude_id']  # Alterado para pegar o username

            nome_paciente = triagem.objects.get(id=nome_paciente_id)

            # Obtém a instância do modelo User com base no username
            profissionalSaude_user = User.objects.get(username=profissionalSaude_id_username)

            # Salva a instância selecionada de Medico_atendimento no modelo Chamar_P_para_atendimento
            Chamar_P_para_atendimento.objects.create(nome_paciente=nome_paciente, profissionalSaude_id=profissionalSaude_user)

            messages.success(self.request, self.success_message)

            # Redireciona para 'Medicos:medico_atendimento' com os kwargs desejados
            return redirect('Triagem:triagem-enfermaria-update', pk=pk)
        else:
            # Lida com erros de formulário, se necessário
            pass
