from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-info/', views.product_info, name='product-info'),
    path('all-orders/', views.AllOrderListView.as_view(), name='all-order-list'),
]