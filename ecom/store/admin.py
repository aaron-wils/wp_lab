from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem, ShippingAddress

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
