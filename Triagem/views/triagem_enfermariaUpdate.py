
from django.contrib.auth.decorators import user_passes_test
#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from Triagem.models import  triagem
from Triagem.forms import TriagemEnfermariaUpdateForm
from django.contrib.auth.models import Group
#from .forms import MedicoSignUpForm
from Medicos.models import CustomUser


# Recebe o Id da view 'triagem_enfermaria' e busca o restante dos campos para serem preenchidos e redireciona para verificar se o paciente possui alergia
class triagem_enfermariaUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = triagem
    form_class = TriagemEnfermariaUpdateForm
    #fields = fields = ['frequencia_cardiaca_FC', 'pressao_arterial_PA_2', 'pressao_arterial_PA', 'frequencia_respiratoria_FR', 'saturacao_de_oxigenio_SPO2', 'hemoglicoteste_HGT', 'temperatura_TEMP', 'peso', 'altura', 'observacao']
    template_name = 'Triagem/triagem.html'
    success_message = "Avaliação Concluída ✔️ Sinais vitais registrados com sucesso!👩‍⚕️"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['nome_paciente'] = self.object.paciente_triagem.paciente_envio_triagem.nome_social        
        context ['tipo_select'] = 'Pré-atendimento'
        context['triagem_andamento'] = "ok" 
        return context

    # Pega o valor do id do paciente no model envio_triagem

    def form_valid(self, form):
        hora = self.object.paciente_triagem.horario_triagem
        data = self.object.paciente_triagem.data_envio_triagem
        self.object.hora_envio_a_classificao = hora
        self.object.data_envio_a_classificao = data

        self.object = form.save(commit=False)
        nome = self.request.user.first_name
        sobrenome = self.request.user.last_name
        self.object.nome_da_enfermeira = f'{nome} {sobrenome}'
        enfermeira = CustomUser.objects.filter(user_id=self.request.user.id).first()

        if enfermeira:
            enf_grupo = enfermeira.grupo_id
            coren = enfermeira.crm
            enf_grupo = Group.objects.filter(id=enf_grupo).first()

            if enf_grupo:
                if enf_grupo.name == 'group_Enfermagem':
                    enf_grupo = "Enfermagem"
                elif enf_grupo.name == 'group_Tec_Enfermagem':
                    enf_grupo = 'Tecnico em enfermagem'
                elif enf_grupo.name == 'group_UPA-Admin':
                    enf_grupo = 'Administrador'
                else:
                    enf_grupo = 'Não pertence a nenhum grupo'
            else:
                enf_grupo = "Super Administrador"

            self.object.nome_da_enfermeira = f'{nome} {sobrenome} | {enf_grupo} coren nº: {coren}'
        self.object.save()
        return super().form_valid(form)

        
    def get_success_url(self):
        pk_envio_triagem = self.object.paciente_triagem.id
        hora = self.object.paciente_triagem.horario_triagem.strftime('%H:%M:%S')
        data = self.object.paciente_triagem.data_envio_triagem.strftime('%Y-%m-%d')
        paciente_envio_triagem_id = self.object.paciente_triagem.paciente_envio_triagem_id

        # Adicione os parâmetros diretamente na string da URL
        url = reverse_lazy('Triagem:triagem-enfermaria-alergia-update', args=[pk_envio_triagem, hora, data, paciente_envio_triagem_id])

        return url


 
