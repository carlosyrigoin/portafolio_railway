from ipware import get_client_ip
from django.http import HttpResponse
from .models import Visitas

def register_ip(get_response):
    def middleware(request):
        ip, is_routable = get_client_ip(request)
        response = get_response(request)
        register = Visitas(ip=ip)
        if register:
            register.save()
        return response   
    return middleware
