from django.contrib import admin
from .models import Product,Offer
from .models import Product,Brand
from .models import Product,Order


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('shoe_name', 'shoe_id', 'user_id', 'address', 'amount', 'order_date')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Brand, BrandAdmin)