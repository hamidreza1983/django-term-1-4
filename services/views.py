from django.shortcuts import render, get_object_or_404, redirect
from .models import Services
from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView

class ServicesView(ListView):
    model = Services
    template_name = 'services/services.html'
    context_object_name = "services"
    paginate_by = 1
    #queryset = Services.objects.filter(status=True)#
    def get_queryset(self):
        if self.kwargs.get("category"):
            services = self.model.objects.filter(category__title=self.kwargs.get("category"), status=True)
        elif self.kwargs.get("name"):
            services = Services.objects.filter(creator__user__email=self.kwargs.get("name"), status=True)
        elif self.request.GET.get("search"):
            search = self.request.GET.get("search")
            services = self.model.objects.filter(content__contains=search, status=True)
        else:
            services = Services.objects.filter(status=True)#
        return services
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first = 1
        service_paginate = Paginator(self.get_queryset(), 1)
        last = service_paginate.num_pages
        context ['first'] = first
        context ['last'] = last
        return context
    

#def services(request, **kwargs):
#     
#    if request.user.is_authenticated and request.user.is_verified:
#        if kwargs.get("category"):
#            service = Services.objects.filter(category__title=kwargs.get("category"), status=True)
#        
#        elif kwargs.get("name"):
#            service = Services.objects.filter(creator__user__username=kwargs.get("name"), status=True)
#        
#        elif request.GET.get("search"):
#            search = request.GET.get("search")
#            service = Services.objects.filter(content__contains=search, status=True)
#        
#        else:
#            service = Services.objects.filter(status=True)
#        
#        service_paginate = Paginator(service, 3)
#        first_page = 1
#        last_page = service_paginate.num_pages
#        try:
#            page_number = request.GET.get("page")
#            service = service_paginate.get_page(page_number)
#        except:
#            page_number = first_page
#            service = service_paginate.get_page(first_page)
#    
#        context = {
#            "services":service,
#            "first" : first_page,
#            "last" : last_page
#        }
#    
#        return render(request, 'services/services.html', context=context)
#    else:
#        return render(request, 'registration/login.html')

   




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

class ServiceDetails(DetailView):
    template_name = 'services/service-details.html'
    model = Services

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        id = self.kwargs['pk']
        service = get_object_or_404(Services, id=id)
        context['comments'] = Comments.objects.filter(status=True, service=service.id)
        return context
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                    id = self.kwargs['pk']
                    service = get_object_or_404(Services, id=id)
                    comment = form.save(commit=False)
                    comment.service = service
                    comment.name = request.user
                    comment.save()
                    messages.add_message(request, messages.SUCCESS, " اوکی ")
                    return redirect(request.path_info)
            else:
                    messages.add_message(request, messages.ERROR, " اوکی no")
                    return redirect(request.path_info)
        else:
            return redirect("accounts:login")
        



        
#    def form_valid(self, form, **kwargs):
#        id = self.kwargs['pk']
#        service = get_object_or_404(Services, id=id)
#        comment = form.save(commit=False)
#        comment.service = service
#        comment.name = self.request.user
#        comment.save()
#        messages.add_message(self.request, messages.SUCCESS, " اوکی ")
#        return redirect(self.request.path_info)
    

#        
#def services_detail(request, id):
#    service = get_object_or_404(Services, id=id)
#    form  = CommentForm()
#    comments = Comments.objects.filter(status=True, service=service.id)
#    context = {
#                'service' : service,
#                "form" : form,
#                "comments" : comments
#            }
#    
#    if request.method == "POST":
#        if request.user.is_authenticated:
#            form = CommentForm(request.POST)
#            if form.is_valid():
#                comment = form.save(commit=False)
#                comment.service = service
#                comment.name = request.user
#                comment.save()
#                messages.add_message(request, messages.SUCCESS, " اوکی ")
#                return redirect(request.path_info)
#            else:
#                messages.add_message(request, messages.ERROR, " اوکی no")
#                return redirect(request.path_info)
#        else:
#            return redirect("accounts:login")
#    else:
#        return render(request, 'services/service-details.html', context=context)
