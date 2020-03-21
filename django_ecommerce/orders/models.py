from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from djmoney.models.fields import MoneyField
from ecommerce.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, related_name='user_orders', on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    shipping_carrier = models.CharField(max_length=20)
    shipping_cost = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    payment_method = models.CharField(max_length=20)
    discount = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    grand_total = MoneyField(max_digits=12, decimal_places=2, default_currency='USD')
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.id} | {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    product = models.ForeignKey(Product, on_delete=models.SET(value='Product has been deleted'))
    price = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    qty = models.PositiveIntegerField()
    discount = MoneyField(max_digits=4, decimal_places=2, default_currency='USD')
    grand_total = MoneyField(max_digits=12, decimal_places=2, default_currency='USD')

    def __str__(self):
        return f"{self.order.id} Order Item"

