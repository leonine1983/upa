from django.forms.forms import BaseForm
from django.http.response import HttpResponse
from Medicos.models import Chamar_P_para_atendimento
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

class Update_chama_usuario(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Chamar_P_para_atendimento
    fields = ['chamado']
    success_message = "👤 Paciente apresentou-se ao atendimento"
    
    def form_valid(self, form):
        return super().form_valid(form)
    





    """
    
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
            return redirect('Medicos:dados do paciente', pk=pk)
        else:
            # Lida com erros de formulário, se necessário
            pass
    
    
    """