from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Max, Min
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from apps.core.models import Order, Product
from apps.core.serializers import OrderSerializer, ProductSerializer, ProductInfoSerializer

# Product list view (function-based view)
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product detail view (function-based view)
@api_view(['GET'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
# Product lists view (function-based view with shortcut)
@api_view(['GET'])
def product_list_shortcut(request):
    products = get_list_or_404(Product)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product detail view (function-based view with shortcut)
@api_view(['GET'])
def product_detail_shortcut(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product detail view (function-based view with shortcut)
@api_view(['GET'])
def product_detail_shortcut(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product info view (function-based view)
@api_view(['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': products.count(),
        'max_price': products.aggregate(max_price = Max('price'))['max_price'],
        'min_price': products.aggregate(min_price = Min('price'))['min_price']
    })
    return Response(serializer.data, status=status.HTTP_200_OK)

# All order list view (function-based view)
@api_view(['GET'])
def all_order_list(request):
    orders = Order.objects.prefetch_related('order_items', 'order_items__product').all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Product list view (class-based view)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []  # Allow unrestricted access

# Product detail view (class-based view)
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []  # Allow unrestricted access
