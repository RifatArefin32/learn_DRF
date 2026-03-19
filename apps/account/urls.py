from django.urls import path, include
from apps.account import views

urlpatterns = [
    path('users/', views.UserListApiView.as_view(), name='user-list'),
    path('register/', views.UserRegistrationView.as_view(), name='user-register'),
    path('login/', views.UserLoginView.as_view(), name='user-login'),
]