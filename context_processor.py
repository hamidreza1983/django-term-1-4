from services.models import Category
from accounts.models import Profile, User



def general_context(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        profile = None
    context = {
        'categories' : Category.objects.all(),
        "profile" : profile,
    }
    return context