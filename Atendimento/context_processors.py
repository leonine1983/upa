from .models import Licenca
from django.contrib.auth.models import User
from django.utils import timezone

def licenca_context(request):
    licenca_ativa = Licenca.objects.filter(ativa=True, expiracao__gt=timezone.now()).first()
    if licenca_ativa is None:
        # Obtem o super
        superuser = User.objects.get(is_superuser = True)
        # Percorrer todos os usuario e desativando-os
        for user in User.objects.exclude(pk=superuser.pk):
            user.is_active = False
            user.save()

    return {'licenca_ativa': licenca_ativa}