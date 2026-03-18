from django.urls import path
from apps.core.views import product_list, product_detail, product_list_shortcut, product_detail_shortcut

urlpatterns = [
    path('products/', product_list, name='product-list'),
    path('products/<int:pk>', product_detail, name='product-detail'),
    path('products/shortcut', product_list_shortcut, name='product-list-shortcut'),
    path('products/shortcut/<int:pk>', product_detail_shortcut, name='product-detail-shortcut'),
]