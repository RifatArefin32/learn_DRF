from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Max, Min
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status, permissions, filters, pagination
from django_filters.rest_framework import DjangoFilterBackend
from apps.core.filters import AllOrderFilter, ProductFilter, FilterOrdersByUser
from apps.core.models import Order, Product
from apps.core.paginations import AllOrdersListPagination
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
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'description']
    pagination_class = pagination.LimitOffsetPagination
    pagination_class.default_limit = 10
    pagination_class.max_limit = 100
    pagination_class.limit_query_param = 'limit' # Optional: Change the query parameter for limit (default is 'limit')
    pagination_class.offset_query_param = 'offset' # Optional: Change the query parameter for offset (default is 'offset')

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return []

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
    filterset_class = AllOrderFilter
    pagination_class = AllOrdersListPagination

# My order list view (class-based view)
class MyOrderListView(generics.ListAPIView):
    queryset = Order.objects.prefetch_related('order_items', 'order_items__product').all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated] 
    filter_backends = [filters.OrderingFilter, FilterOrdersByUser]
    ordering_fields = ['created_at', 'status']
    ordering = ['-created_at']  # Default ordering

    # def get_queryset(self):
    #     user = self.request.user
    #     return Order.objects.filter(user=user).prefetch_related('order_items', 'order_items__product')

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