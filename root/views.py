from django.shortcuts import render, redirect
from .models import Agents, Testimonials
from services.models import Services, Category
from django.contrib.auth.decorators import login_required


from django.http import HttpResponse


#@login_required
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


from .models import ContactUs
from .forms import ContactUsForm
from django.contrib import messages
#def contactus(request):
#    if request.method == "POST":
#        form =  ContactUsForm(request.POST)
#        if form.is_valid():
#            contact = ContactUs()
#            contact.name = request.POST.get("name")
#            contact.email = request.POST.get("email")
#            contact.subject = request.POST.get("subject")   
#            contact.message = request.POST.get("message")
#            contact.save()
#            messages.add_message(request, messages.SUCCESS, "your contact received successfully")
#            return render(request,"root/contact.html")
#        else:
#            messages.add_message(request, messages.ERROR, "your input data is not valid")
#            return render(request,"root/contact.html")
#    else:
#        return render(request,"root/contact.html")

def contactus(request):
    if request.method == "POST":
        form =  ContactUsForm(request.POST)
        if request.user.is_authenticated and request.user.has_perm("sites.view_site"):
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "your contact received successfully")
                return render(request,"root/contact.html")
            else:
                messages.add_message(request, messages.ERROR, "your input data is not valid")
                return render(request,"root/contact.html")
        else:
            messages.add_message(request, messages.ERROR, "sharmondeh shoma bayad doctor bashid")
            return render(request,"root/contact.html")

    else:
        form = ContactUsForm()
        context = {'form': form}
        return render(request,"root/contact.html", context=context)
    
        # if request.user.is_authenticated and request.user.has_perm("sites.view_site"):
        #     form = ContactUsForm()
        #     context = {'form': form}
        #     return render(request,"root/contact.html", context=context)
        # else:
        #     return redirect("accounts:login")


def aboutus(request):
    return render(request,"root/about.html")

def agent(request):
    #agents = Agents.objects.all()
    agents = Agents.objects.filter(status=True)
    return render(request,"root/agents.html", context={"agents":agents} )
