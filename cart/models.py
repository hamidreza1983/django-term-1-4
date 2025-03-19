from django.db import models
from accounts.models import User

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    postal_code = models.CharField(max_length=10)
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    zarinpal_authority = models.CharField(max_length=100, blank=True, null=True)
    zarinpal_refid = models.CharField(max_length=100, blank=True, null=True)
    zarinpal_data = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Order {self.id}"
    
    def total_price(self):
        total = 0
        for item in self.items.all():
            total += item.price * item.quantity
        return total

    def __iter__(self):
        for item in self.items.all():
            yield item

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    service = models.ForeignKey('services.Services', on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.service.title}"