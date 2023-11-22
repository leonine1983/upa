from .models import Licenca
from django.utils import timezone

def licenca_context(request):
    licenca_ativa = Licenca.objects.filter(ativa=True, expiracao__gt=timezone.now()).first()
    return {'licenca_ativa': licenca_ativa}