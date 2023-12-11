# views.py
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View
from Medicos.forms import ChamarPacienteForm
from Medicos.models import Chamar_P_para_atendimento, Medico_atendimento

class MedicoChamaPacienteView(SuccessMessageMixin, View):
    template_name = 'seu_template.html'  # Substitua pelo nome real do seu template
    success_message = "Paciente chamado com sucesso"

    def post(self, request, pk):
        form = ChamarPacienteForm(request.POST)
        if form.is_valid():
            nome_paciente_id = form.cleaned_data['nome_paciente']
            nome_paciente = Medico_atendimento.objects.get(id=nome_paciente_id)

            # Salva a instância selecionada de Medico_atendimento no modelo Chamar_P_para_atendimento
            Chamar_P_para_atendimento.objects.create(nome_paciente=nome_paciente)

            messages.success(self.request, self.success_message)

            # Redireciona para 'Medicos:medico_atendimento' com os kwargs desejados
            
            return redirect('Medicos:dados do paciente', pk=pk)
        else:
            # Lida com erros de formulário, se necessário
            pass
