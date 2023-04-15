from datetime import datetime, date

from django.contrib.auth.decorators import user_passes_test
#Restringir acesso
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

from Atendimento.models import envio_triagem

from .models import Classifica_risco_model, triagem
from .forms import TriagemEnfermariaForm


class triagem_enfermaria(CreateView):
    model = triagem
    form_class = TriagemEnfermariaForm
    template_name = 'Triagem/triagem.html'    
    success_url =reverse_lazy('Triagem:triagem-enfermaria')

    def get_success_url(self):
        obj_ultimo = triagem.objects.latest('pk').id
        obj_EnvioTriagem = triagem.objects.filter(pk=obj_ultimo)
        for pk in obj_EnvioTriagem:
            id = pk.paciente_triagem_id
            id = int(id)
        return reverse('Triagem:triagem_concluida', kwargs={'pk':id})

    

class triagem_concluida_Update(LoginRequiredMixin, UpdateView):
    model = envio_triagem
    fields = ['triagem_concluida']
    template_name = 'Triagem/triagem_confirm_final.html'
    success_url =reverse_lazy('Triagem:triagem-enfermaria')


def chamar_paciente_triagem(request, pk):
    data = envio_triagem.objects.filter(pk = pk)   
    return render(request, 'Triagem/chamar_paciente.html',
                  {
        'data_triagem' : data
                  })

#Classificação de risco
class Classifica_risco_view(LoginRequiredMixin, CreateView):
    model = Classifica_risco_model
    fields = ['classifica_tipo', 'descri']
    template_name = 'Triagem/classifica_risco.html'
    success_url = reverse_lazy('Triagem:triagem-enfermaria')


class Classifica_risco_lista_view(LoginRequiredMixin, ListView):
    model = Classifica_risco_model
    template_name =  'Triagem/classifica_risco.html'
    paginate_by =12

class Classifica_risco_Update_view(LoginRequiredMixin, UpdateView):
    model = Classifica_risco_model    
    fields = ['classifica_tipo', 'descri']
    template_name =  'Triagem/classifica_risco.html'
    success_url = reverse_lazy('Triagem:classifica-risco-lista')






from django.http import JsonResponse
from django.shortcuts import render

from .models import ChamarPaciente


def sua_view(request):
  print(f'verificar o que esta vindo pelo request.post. aqui é o resultado: {request.POST}')
  if request.method == 'POST':
    id_paciente = request.POST['paciente_id']
    nome_paciente = request.POST['nome_paciente']
    novo_chamado = ChamarPaciente(id_paciente=id_paciente, nome_paciente=nome_paciente)
    novo_chamado.save()
    return JsonResponse({'status': 'ok'})
  return render(request, 'sua_template.html')


  # xxxxxxxxxxxxxxxxx CRIA USUARIOS ENFERMAGE E TEC XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX




from django import forms
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.shortcuts import redirect, render

#from .forms import MedicoSignUpForm
from Medicos.models import CustomUser
import time


class MedicoSignUpForm(forms.ModelForm):    
    telefone = forms.CharField(max_length=20)
    data_nascimento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'readonly': 'readonly'}))

    endereco = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o nome da rua'}), label='Rua')
    crm = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o nº COREN'}), label="nº COREN")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'crm', 'endereco')




# Cria USUARIOS do tipo MEDICOS ----------------------------------------------
def Enferm_SignUpForm(request):
    if request.method == 'POST':
        form = MedicoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            grupo = request.POST.get('grupo')
            

            if grupo == 'group_Enfermagem':
                print(f'isse esta sendo enviado {grupo}')
                group = Group.objects.get(name='group_Enfermagem')
            elif grupo == 'group_Tec_Enfermagem':
                group = Group.objects.get(name='group_Tec_Enfermagem')

            custom_user = CustomUser.objects.create(
                user=user,
                telefone=form.cleaned_data['telefone'],
                data_nascimento=form.cleaned_data['data_nascimento'],
                endereco=form.cleaned_data['endereco'],
                crm=form.cleaned_data['crm'],  # novo campo
                grupo=group
            )

            group.user_set.add(user)  # Adiciona o usuário ao grupo
            messages.success(request, 'Usuário criado com sucesso.')
            return redirect('Triagem:user_create')
    else:
        form = MedicoSignUpForm()

    # Aqui, você pode incluir os campos adicionais na consulta ao banco de dados
    medicos_group = Group.objects.get(name='group_Medicos')
    group_UPA_Admin = Group.objects.get(name='group_UPA-Admin')
    users = CustomUser.objects.exclude(user__groups=medicos_group).exclude(user__groups=group_UPA_Admin).select_related('user').values(
        'id', 'user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )
    return render(request, 'Triagem/cria_enfEtec/cria_enfEtec.html', {
        'form': form,
        'users': users,
    })


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from Medicos.models import CustomUser


class EnfermUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = MedicoSignUpForm
    template_name = 'Triagem/cria_enfEtec/cria_enfEtec.html'
    success_message = 'Usuário atualizado com sucesso.'
    success_url = reverse_lazy('Triagem:user_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medicos_group = Group.objects.get(name='group_Medicos')
        group_UPA_Admin = Group.objects.get(name='group_UPA-Admin')
        users = CustomUser.objects.exclude(user__groups=medicos_group).exclude(user__groups=group_UPA_Admin).select_related('user').values(
        'id', 'user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )        
        context['users'] = users
        pk = self.kwargs['pk']

        context['up'] = f'{CustomUser.objects.get(pk=pk).user.first_name} {CustomUser.objects.get(pk=pk).user.last_name}'
        return context
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object.user # adiciona o usuário atual ao formulário
        return kwargs

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        grupo = self.request.POST.get('grupo')

        if grupo == 'group_Enfermagem':
            group = Group.objects.get(name='group_Enfermagem')
        elif grupo == 'group_Tec_Enfermagem':
            group = Group.objects.get(name='group_Tec_Enfermagem')

        custom_user = CustomUser.objects.get(user=self.object.user)
        custom_user.telefone = form.cleaned_data['telefone']
        custom_user.data_nascimento = form.cleaned_data['data_nascimento']
        custom_user.endereco = form.cleaned_data['endereco']
        custom_user.crm = form.cleaned_data['crm']
        custom_user.grupo = group
        custom_user.save()

        custom_user.user.groups.clear()
        custom_user.user.groups.add(group)

        return redirect(self.success_url)
    
    

from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import Group


class DeleteUserDelet(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    template_name = 'Triagem/cria_enfEtec/cria_enfEtec _delete.html' 
    success_message = 'Usuário excluído com sucesso.'
    success_url = reverse_lazy('Triagem:user_create')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.user.delete()
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        medicos_group = Group.objects.get(name='group_Medicos')
        group_UPA_Admin = Group.objects.get(name='group_UPA-Admin')
        users = CustomUser.objects.exclude(user__groups=medicos_group).exclude(user__groups=group_UPA_Admin).select_related('user').values(
        'id', 'user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )        
        context['users'] = users
        pk = self.kwargs['pk']

        context['up'] = f'{CustomUser.objects.get(pk=pk).user.first_name} {CustomUser.objects.get(pk=pk).user.last_name}'
        return context

    
