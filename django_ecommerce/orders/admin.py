from django.contrib import admin
from .models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    list_filter = ['created_at']


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ['created_at']


admin.site.register(OrderItem, OrderItemAdmin)