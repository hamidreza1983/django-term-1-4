from django.shortcuts import render, get_object_or_404
from .models import Services
from django.core.paginator import Paginator

def services(request, **kwargs):

    
    if kwargs.get("category"):
        service = Services.objects.filter(category__title=kwargs.get("category"), status=True)
        
    elif kwargs.get("name"):
        service = Services.objects.filter(creator__user__username=kwargs.get("name"), status=True)
        
    elif request.GET.get("search"):
        search = request.GET.get("search")
        service = Services.objects.filter(content__contains=search, status=True)
        
    else:
        service = Services.objects.filter(status=True)
        
    service_paginate = Paginator(service, 1)
    first_page = 1
    last_page = service_paginate.num_pages

    try:
        page_number = request.GET.get("page")
        service = service_paginate.get_page(page_number)
    except:
        page_number = first_page
        service = service_paginate.get_page(first_page)
    
    context = {
        "services":service,
        "first" : first_page,
        "last" : last_page
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


from .forms import CommentForm
from django.contrib import messages
from .models import Comments
def services_detail(request, id):
    service = get_object_or_404(Services, id=id)
    form  = CommentForm()
    comments = Comments.objects.filter(status=True, service=service.id)
    context = {
                'service' : service,
                "form" : form,
                "comments" : comments
            }
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.service = service
           comment.save()
           messages.add_message(request, messages.SUCCESS, " اوکی ")
           return render(request, 'services/service-details.html', context=context)
        
        else:
           messages.add_message(request, messages.ERROR, " اوکی no")
           return render(request, 'services/service-details.html', context=context)
    else:
        return render(request, 'services/service-details.html', context=context)
