from django.shortcuts import render, get_object_or_404
from .models import Services

def services(request):
    service = Services.objects.filter(status=True)
    context = {
        "services": service
    }
    return render(request, 'services/services.html', context=context)




#def services_detail(request, id):
#    id = request.GET.get('id')
#    service = get_object_or_404(Services, id=id)
#    context = {
#            'service' : service,
#        }
#    return render(request, 'services/service-details.html', context=context)

    #try:
    #    service = Services.objects.get(id=id)
    #    context = {
    #        'service' : service,
    #    }
    #    return render(request, 'services/service-details.html', context=context)
    #except:
    #    return render(request, '404.html')

def services_detail(request, id):
    service = get_object_or_404(Services, id=id)
    context = {
            'service' : service,
        }
    return render(request, 'services/service-details.html', context=context)
