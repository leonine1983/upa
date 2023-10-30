from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.shortcuts import  redirect, render
from Atendimento.models import *
from Medicos.models import CustomUser
from django import forms


class MedicoSignUpForm(forms.ModelForm):
    telefone = forms.CharField(max_length=20)
    
    data_nascimento = forms.DateField()

    endereco = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder':'Digite o nome da rua'}), label='Rua')
    crm = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Digite o CRM'}), label="CRM")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'crm', 'endereco')



# Cria USUARIOS do tipo MEDICOS ----------------------------------------------
def medico_signup(request):
    if request.method == 'POST':
        form = MedicoSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            group = Group.objects.get(name='group_Medicos')

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
            return redirect('Medicos:medico_signup')
    else:
        form = MedicoSignUpForm()

    # Aqui, você pode incluir os campos adicionais na consulta ao banco de dados
    medicos_group = Group.objects.get(name='group_Medicos')
    users = CustomUser.objects.filter(user__groups=medicos_group).select_related('user').values(
        'id','user__id', 'user__username', 'user__first_name', 'user__last_name', 'user__email',
        'telefone', 'data_nascimento', 'endereco','user__groups__name', 'crm'
    )
    

    return render(request, 'Medicos/criar_medicos/criar_medico.html', {
        'form': form,
        'users': users,
    })
