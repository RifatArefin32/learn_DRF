from django.contrib import admin
from .models import Product, Order, OrderItem

# Register Order model with related OrderItem inline
class OrderItemInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_id', 'user__username')
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)


# Register Product model with custom admin interface
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_in_stock')
    search_fields = ['name']
    list_filter = ['stock']

admin.site.register(Product, ProductAdmin)


# Register OrderItem model for direct access in admin
admin.site.register(OrderItem)

