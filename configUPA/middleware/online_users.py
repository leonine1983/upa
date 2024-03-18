from django.utils import timezone
from django.contrib.auth import authenticate

class OnlineUsersMiddleare:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            request.user.last_seen = timezone.now()
            request.user.save()
        return response