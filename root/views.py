from django.shortcuts import render


from django.http import HttpResponse

def home(request):
    return render(request,"root/index.html")

def contactus(request):
    return render(request,"root/contact.html")

def aboutus(request):
    return render(request,"root/about.html")
