from configUPA.models import Notificate_system

def notifications(request):
    if request.user.is_authenticated:
        notification = Notificate_system.objects.filter(user=request.user)
        visto = all(notif.visto for notif in notification)
    else:
        notification = []
        visto = False

    return {'notification': notification, 'visto': visto}
