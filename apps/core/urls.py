from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>', views.product_detail, name='product-detail'),
    path('products/shortcut', views.product_list_shortcut, name='product-list-shortcut'),
    path('products/shortcut/<int:pk>', views.product_detail_shortcut, name='product-detail-shortcut'),
    path('product-info/', views.product_info, name='product-info'),
    path('all-orders/', views.all_order_list, name='all-order-list'),
]