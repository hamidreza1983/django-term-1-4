from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from services.models import Services
from django.views.generic import FormView
from .forms import CheckoutForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem

# Create your views here.


# @login_required
def cart_view(request):
    service_list = []
    cart = request.session.get("cart", {})
    for id, quantity in cart.items():
        service = Services.objects.get(id=int(id))
        quantity = int(quantity)
        service_list.append(
            {
                "service": service,
                "quantity": quantity,
                "total_price": service.price * quantity,
            }
        )
    total = 0
    for item in service_list:
        total += item["total_price"]
    context = {"service_list": service_list, "total": total}
    return render(request, "cart/cart.html", context=context)


class CheckoutView(LoginRequiredMixin, FormView):
    template_name = "cart/checkout.html"
    form_class = CheckoutForm

    def form_valid(self, form):
        user = self.request.user
        phone = form.cleaned_data["phone"]
        address = form.cleaned_data["address"]
        postal_code = form.cleaned_data["postal_code"]
        order = Order.objects.create(
            user=user,
            phone=phone,
            address=address,
            postal_code=postal_code,
        )
        cart = self.request.session.get("cart", {})
        for id, quantity in cart.items():
            service = Services.objects.get(id=int(id))
            quantity = int(quantity)
            OrderItem.objects.create(
                order=order,
                service=service,
                price=service.price,
                quantity=quantity,
            )
        payment = self.request.session.get("payment", {})
        payment["order_id"] = order.id
        payment["total_price"] = order.total_price()
        self.request.session["payment"] = payment
        self.request.session.modified = True
        return redirect("payment:request")

    def form_invalid(self, form):
        pass
