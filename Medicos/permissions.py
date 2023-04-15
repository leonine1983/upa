from django.contrib.auth.models import Permission

# Permissões para a visualização da lista de triagem
view_triagem_list = Permission.objects.get(codename='view_triagem')

# Permissões para a criação de triagem
add_triagem = Permission.objects.get(codename='add_triagem')

# Permissões para a visualização de detalhes de triagem
view_triagem_detail = Permission.objects.get(codename='view_triagem')

# Permissões para a atualização de triagem
change_triagem = Permission.objects.get(codename='change_triagem')

# Permissões para a exclusão de triagem
delete_triagem = Permission.objects.get(codename='delete_triagem')
