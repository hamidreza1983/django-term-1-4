from django.shortcuts import render
from .models import Services

def services(request):
    service = Services.objects.filter(status=True)
    context = {
        "services": service
    }
    return render(request, 'services/services.html', context=context)
