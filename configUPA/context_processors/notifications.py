from configUPA.models import Notificate_system

def notifications(request):
    notification = Notificate_system.objects.all()
    visto = True
    for n in notification:
        if n.visto == False:
            visto = False
            break

    return {'notification' : notification,
            'visto': visto}