from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.views.generic import CreateView
#from Medicos.forms import Form_medico_atendimento
from Medicos.models import CustomUser, Medico_atendimento
from Triagem.models import triagem
from Medicos.models import CustomUser


class atendimento_medico_createView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Medico_atendimento
    #Chave Estrangeira 'paciente_medico_atendimento'
    fields = ['paciente_medico_atendimento', 'historico_doenca_atual_HDA', 'exame_fisico', 'Diagnostico', 'conduta','classificacao_internacional_doenca_CID']
    template_name = 'Medicos/medico_atendimento_atendimento.html'   
    success_message = 'Avaliação médica feita com sucesso'
     
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        pk = self.kwargs['pk']    
        context['paciente_medico'] = Medico_atendimento.objects.filter(pk=pk)
        context['triagem'] = triagem.objects.filter(id = pk)
        context['atendimento'] = 'atendimento'        
        return context

    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        
        # Define os campos do objeto Medico_atendimento
        self.object.paciente_medico_atendimento_id = self.kwargs['pk']
        self.object.medico_nome = self.request.user
        
        medico_id = self.request.user.id
        medico_group_id = None  # Valor padrão caso não haja resultado no filtro
        medico_group = CustomUser.objects.filter(user_id=medico_id)
        
        for med in medico_group:
            medico_group_id = med.grupo_id
            crm = med.crm
        
        medico_group = Group.objects.filter(id=medico_group_id)
        
        for med in medico_group:
            medico_group = med.name
            
            if medico_group == "group_Medicos":
                medico_group = "Medico"
            
            #self.object.medico_nome += f' | {medico_group} | CRM nº: {crm}'
            #self.object.medico_nome = self.request.user.username  # Substitua 'username' pelo campo que contém o nome do médico no modelo User
        
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    
    #success_url = reverse_lazy('Medicos:dados do paciente_medicamentos self.kwargs['pk']')
    def get_success_url(self):
        return reverse('Medicos:dados_do_paciente_medicamentos', kwargs={'pk':self.kwargs['pk']})
