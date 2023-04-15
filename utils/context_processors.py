def grupo_usuario(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name='group_Enfermagem').exists():
            grupo = 'group_Enfermagem'
        elif user.groups.filter(name='group_Medicos').exists():
            grupo = 'group_Medicos'
        elif user.groups.filter(name='group_Tec_Enfermagem').exists():
            grupo = 'group_Tec_Enfermagem'
        elif user.groups.filter(name='group_UPA-Admin').exists():
            grupo = 'group_UPA-Admin'
        else:
            grupo = ''
    else:
        grupo = None

    return {'grupo_usuario': grupo}