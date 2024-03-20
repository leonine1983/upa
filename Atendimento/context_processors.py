from .models import Licenca
from django.contrib.auth.models import User
from django.utils import timezone

# Atividade da lincença
def licenca_context(request):
    licenca_ativa = Licenca.objects.filter(ativa=True, expiracao__gt=timezone.now()).first()
    name_sistem = "SG-UPA"
    """
    if licenca_ativa is None:
        # Obtem todos os superusuários
        superusers = User.objects.filter(is_superuser=True)
        # Percorrer todos os usuários superusuários e desativando-os
        
        for superuser in superusers:
            superuser.is_active = True
            superuser.save()
    else:
        # Caso exista uma licença ativa, definir todos os usuários como ativos
        User.objects.update(is_active=True)

    """
    return {'licenca_ativa': licenca_ativa, 'name_sistem':name_sistem}

# Atividade da lincença