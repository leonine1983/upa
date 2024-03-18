from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta



def online_users(request):
    # Filtrar usuários que foram vistos nos últimos 15 minutos
    online_users = User.objects.filter(last_login__gte=timezone.now() - timedelta(minutes=15))
    return {'online_users': online_users}
