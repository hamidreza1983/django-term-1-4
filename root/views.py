from django.shortcuts import render
from .models import Agents, Testimonials
from services.models import Services, Category


from django.http import HttpResponse

def home(request):
    agents = Agents.objects.filter(status=True)[:3]
    services = Services.objects.filter(status=True)[:3]
    testers = Testimonials.objects.filter(status=True)
    context = {
        'services': services,
        'agents' : agents,
        'testers' : testers,
    }
    return render(request,"root/index.html", context=context)

def contactus(request):
    return render(request,"root/contact.html")

def aboutus(request):
    return render(request,"root/about.html")

def agent(request):
    #agents = Agents.objects.all()
    agents = Agents.objects.filter(status=True)
    return render(request,"root/agents.html", context={"agents":agents} )
