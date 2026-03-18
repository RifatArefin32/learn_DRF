from django.urls import path
from apps.core.views import product_list

urlpatterns = [
    path('products/', product_list, name='product-list'),
]
