from django.contrib import admin
from .models import Product, Order, OrderItem, Invoice

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_time')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id' ,'costumer', 'order_date')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id' ,'order', 'product')

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Invoice, InvoiceAdmin)

