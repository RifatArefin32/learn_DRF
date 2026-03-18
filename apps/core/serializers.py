from rest_framework import serializers
from apps.core.models import OrderItem, Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'is_in_stock']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price must be a positive number.")
        return value
    

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = OrderItem
        fields = ['product_name', 'product_price', 'quantity', 'sub_total']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField('sum_total_price')

    def get_total_price(self, obj):
        return sum(item.sub_total for item in obj.order_items.all())

    def sum_total_price(self, obj):
        total = 0
        for item in obj.order_items.all():
            total += item.sub_total
        return total
    
    class Meta:
        model = Order
        fields = ['order_id', 'order_items', 'total_price', 'total', 'created_at', 'status', 'user']


class ProductInfoSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    count = serializers.IntegerField()
    max_price = serializers.DecimalField(max_digits=10, decimal_places=2)   
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)   
    class Meta:
        model = Product
        fields = ['products', 'count', 'max_price', 'min_price']