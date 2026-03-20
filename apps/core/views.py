from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Max, Min
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions
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
class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    # permission_classes = []  # Allow unrestricted access

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return []
    
    def get_queryset(self):
        self.queryset = Product.objects.all()
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')
        min_stock = self.request.query_params.get('min_stock')
        if min_price is not None:
            self.queryset = self.queryset.filter(price__gte=min_price)
        if max_price is not None:
            self.queryset = self.queryset.filter(price__lte=max_price)
        if min_stock is not None:
            self.queryset = self.queryset.filter(stock__gte=min_stock)
        return self.queryset

# Product detail view (class-based view)
class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id' 

    def get_permissions(self):
        if(self.request.method in ['PUT', 'PATCH', 'DELETE']):
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

# All order list view (class-based view)
class AllOrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('order_items', 'order_items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser]

    def filter_queryset(self, queryset):
        if 'status' in self.request.query_params:
            status = self.request.query_params['status']
            queryset = queryset.filter(status=status)
        return queryset


# My order list view (class-based view)
class MyOrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Allow only authenticated users

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(user=user).prefetch_related('order_items', 'order_items__product')

# Class-based view for product info
class ProoductInfoApiView(APIView):
    permission_classes = [permissions.IsAdminUser]  # Allow unrestricted access

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductInfoSerializer({
            'products': products,
            'count': products.count(),
            'max_price': products.aggregate(max_price=Max('price'))['max_price'],
            'min_price': products.aggregate(min_price=Min('price'))['min_price']
        })
        return Response(serializer.data, status=status.HTTP_200_OK)
    
# Class-based view for creating a product
class ProductCreateApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)