from django.contrib import admin
from market.models import Provider, Consumer, Category, Product, Store, Order, OrderProduct

class ProviderAdmin(admin.ModelAdmin):
    pass
admin.site.register(Provider, ProviderAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']

admin.site.register(Product, ProductAdmin)   

class ConsumerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Consumer, ConsumerAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']    
    
admin.site.register(Category, CategoryAdmin)


class StoreAdmin(admin.ModelAdmin):
    pass
admin.site.register(Store, StoreAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['consumer']
    
admin.site.register(Order, OrderAdmin)

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'amount']

admin.site.register(OrderProduct, OrderProductAdmin)

