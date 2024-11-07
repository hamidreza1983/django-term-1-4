from services.models import Category



def general_context(request):
    context = {
        'categories' : Category.objects.all(),
    }
    return context