from django.urls import path
from apps.core import views

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/create/', views.ProductCreateApiView.as_view(), name='product-create'),
    path('products/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-info/', views.ProoductInfoApiView.as_view(), name='product-info'),
    path('all-orders/', views.AllOrderListView.as_view(), name='all-order-list'),
    path('my-orders/', views.MyOrderListView.as_view(), name='my-order-list'),
]