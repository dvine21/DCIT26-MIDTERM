from django.contrib import admin
from .models import Product, Order, OrderItem, Shipping, Payment

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Shipping)
admin.site.register(Payment)
