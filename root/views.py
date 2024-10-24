from django.shortcuts import render
from .models import Agents


from django.http import HttpResponse

def home(request):
    agents = Agents.objects.filter(status=True)[:3]
    return render(request,"root/index.html", context={"agents":agents})
def contactus(request):
    return render(request,"root/contact.html")

def aboutus(request):
    return render(request,"root/about.html")

def agent(request):
    #agents = Agents.objects.all()
    agents = Agents.objects.filter(status=True)
    return render(request,"root/agents.html", context={"agents":agents} )
