from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.core.models import Product
from apps.core.serializers import ProductSerializer

# Product list view (function-based view)
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)