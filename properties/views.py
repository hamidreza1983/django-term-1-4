from django.shortcuts import render

# Create your views here.
def properties(request):
    return render(request, 'properties/properties.html')