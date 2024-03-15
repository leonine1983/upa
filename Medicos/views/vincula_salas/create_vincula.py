from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import  reverse_lazy
from django.views.generic import CreateView
from django.core.paginator import Paginator
from Atendimento.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from Medicos.models import   Salas_Atendimento
from django.contrib.auth.models import Group


# Vicula Medico às SALAS -----------------------------------------------------------------------------
class VinculaProfissiona_sala_view(LoginRequiredMixin, CreateView):
    model = Salas_Atendimento
    fields = ['nomeSala', 'profissionalSaude']
    template_name = 'Medicos/salas/salas.html'
    success_url = reverse_lazy('Medicos:salasProfissionalCreate')
    paginate_by = 5

    def get_initial(self):
        initial = super().get_initial()
        # Set the initial value of profissionalSaude to the logged-in user
        initial['profissionalSaude'] = self.request.user
        return initial

    def form_valid(self, form):
        sala = form.save(commit=False)
        profissional = sala.profissionalSaude
        if profissional.groups.filter(name='group_Medicos').exists():
            messages.success(self.request, f"O profissional, {profissional}, foi vinculado à sala {sala} com sucesso.")
            
            self.success_url = reverse_lazy('Medicos:medico_prontuario')
        elif profissional.groups.filter(name='group_Enfermagem').exists():
            
            messages.success(self.request, f"O profissional, {profissional}, vinculado à sala {sala} com sucesso.")
            self.success_url = reverse_lazy('Triagem:triagem-enfermaria')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['salaProfissional'] = 'vinculaSala'
        paginator = Paginator(Salas_Atendimento.objects.all(), self.paginate_by)
        page_number = self.request.GET.get('page')  # Obtenha o número da página da URL
        context["vinculo_sala"] = 'ok'
        context['object_list'] = paginator.get_page(page_number)
        return context
    
