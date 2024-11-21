from django.contrib import admin
from .models import Category, UnitCategory, Product, Customer, Cart, CartItem, Order, Payment, OrderItem


admin.site.register(Category)
admin.site.register(UnitCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)