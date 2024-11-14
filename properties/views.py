from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def properties(request):
    context = {
        'properties': Properties.objects.filter(status=True)
    }
    return render(request, 'properties/properties.html', context=context)


def property_detail(request, id):
    property = get_object_or_404(Properties, id=id)
    context = {
        'property' : property,
    }
    return render(request, 'properties/property-single.html', context=context)
