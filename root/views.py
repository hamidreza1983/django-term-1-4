from django.shortcuts import render, redirect
from .models import Agents, Testimonials
from services.models import Services, Category
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import ContactUs
from .forms import ContactUsForm
from django.contrib import messages
from django.http import HttpResponse
import time
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


#method_decorator(cache_page(60 * 2), name="dispatch")
class HomeView(TemplateView):
    template_name = "root/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        services = Services.objects.filter(status=True)[:3]
        services_cache = cache.get("services")
        if services_cache is None:
            cache.set("services", services, 60 * 2)
        context["services"] = cache.get("services")
        context["agents"] = Agents.objects.filter(status=True)[:3]
        context["testers"] = Testimonials.objects.filter(status=True)
        return context




# @login_required
# def home(request):
#     agents = Agents.objects.filter(status=True)[:3]
#     services = Services.objects.filter(status=True)[:3]
#     testers = Testimonials.objects.filter(status=True)
#     context = {
#         'services': services,
#         'agents' : agents,
#         'testers' : testers,
#     }
#     return render(request,"root/index.html", context=context)

from .tasks import send_email
# @cache_page(60 * 2)
def test(request):
    send_email.delay()
    return HttpResponse("<h1>hello cache</h1>")

# def contactus(request):
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
#            return render@method_decorator(cache_page(60 * 2), name="dispatch")(request,"root/contact.html")
#        else:
#            messages.add_message(request, messages.ERROR, "your input data is not valid")
#            return render(request,"root/contact.html")
#    else:
#        return render(request,"root/contact.html")
def contactusapi(request):
    return render (request, "root/contact-api.html")

@cache_page(60 * 2)
def contactus(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if request.user.is_authenticated and request.user.has_perm(
            "sites.view_site"
        ):
            if form.is_valid():
                form.save()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "your contact received successfully",
                )
                return render(request, "root/contact.html")
            else:
                messages.add_message(
                    request, messages.ERROR, "your input data is not valid"
                )
                return render(request, "root/contact.html")
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "sharmondeh shoma bayad doctor bashid",
            )
            return render(request, "root/contact.html")

    else:
        form = ContactUsForm()
        context = {"form": form}
        return render(request, "root/contact.html", context=context)

        # if request.user.is_authenticated and request.user.has_perm("sites.view_site"):
        #     form = ContactUsForm()
        #     context = {'form': form}
        #     return render(request,"root/contact.html", context=context)
        # else:
        #     return redirect("accounts:login")


class AboutView(TemplateView):
    template_name = "root/about.html"


# def aboutus(request):@method_decorator(cache_page(60 * 2), name="dispatch")
#     return render(request,"root/about.html")

@method_decorator(cache_page(60 * 2), name="dispatch")
class AgentsView(TemplateView):
    template_name = "root/agents.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agents"] = Agents.objects.filter(status=True)


# def agent(request):
#     #agents = Agents.objects.all()
#     agents = Agents.objects.filter(status=True)
#     return render(request,"root/agents.html", context={"agents":agents} )


class GoogleView(RedirectView):
    url = "https://google.com"
