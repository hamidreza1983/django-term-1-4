from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from services.models import Services

# Create your views here.

#@login_required
def cart_view(request):
    service_list=[]
    cart = request.session.get("cart", {})
    for id , quantity in cart.items():
        service = Services.objects.get(id=int(id))
        quantity = int(quantity)
        service_list.append({
            "service": service, 
            "quantity": quantity, 
            "total_price": service.price * quantity})
    total = 0
    for item in service_list:
        total += item["total_price"]
    context = {
        "service_list": service_list,
        "total": total
    }
    return render(request, 'cart/cart.html', context=context)