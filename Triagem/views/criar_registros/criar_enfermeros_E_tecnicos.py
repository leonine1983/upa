from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from .MedicoSignUpForm import *

#from .forms import MedicoSignUpForm
from Medicos.models import CustomUser


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
