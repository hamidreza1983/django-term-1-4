from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests
from cart.models import Order


ZP_API_REQUEST = (
    "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
)
ZP_API_VERIFY = (
    "https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
)
ZP_API_STARTPAY = "https://sandbox.zarinpal.com/pg/StartPay/"
CALLBACK_URL = "http://127.0.0.1:8000/payment/verify/"

MERCHANT_ID = "000000000000-0000-0000-0000-000000000000"


class PaymentRequestView(TemplateView):

    def get(self, request, *args, **kwargs):
        price = request.session.get("payment", {}).get("total_price", 0)
        data = {
            "MerchantID": MERCHANT_ID,
            "Amount": int(price),
            "Description": "پرداخت مبلغ سفارش",
            "CallbackURL": CALLBACK_URL,
        }
        try:
            response = requests.post(ZP_API_REQUEST, data=data)
            response = response.json()
            if response.get("Status") == 100:
                return redirect(
                    ZP_API_STARTPAY + response.get("Authority")
                )
            return render(
                request,
                "payment/error.html",
                context={"error": response.get("Status")},
            )
        except:
            return render(
                request,
                "payment/error.html",
                context={"error": "خطا در ارتباط با زرین پال"},
            )


class PaymentVerifyView(TemplateView):

    def get(self, request, *args, **kwargs):
        authority = request.GET.get("Authority")
        price = request.session.get("payment", {}).get("total_price", 0)
        data = {
            "MerchantID": MERCHANT_ID,
            "Authority": authority,
            "Amount": int(price),
        }
        response = requests.post(ZP_API_VERIFY, data=data)
        response = response.json()
        if response.get("Status") == 100 or response.get("Status") == 101:
            order_id = request.session.get("payment", {}).get("order_id")
            order = Order.objects.get(id=order_id)
            order.is_paid = True
            order.save()
            return render(request, "payment/success.html")
        else:
            return render(
                request,
                "payment/error.html",
                context={"error": response.get("Status")},
            )


# Create your views here.
