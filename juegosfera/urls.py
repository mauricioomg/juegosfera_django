"""juegosfera URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path, include 
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken import views
from apps.index.views import Register, RegisterProduct, UpdateProduct, DeleteProduct


urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('index/', include(('apps.index.urls','index'))),
    
    path('index_generate_token/', views.obtain_auth_token),
    #path('accounts/login/', Login.as_view(), name = 'login'),
    #path('logout/', Logout, name = 'logout'),
    #path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('register/', Register.as_view(), name = 'register'),
    path('create_product/', RegisterProduct.as_view(), name = 'create_product'),
    path('update_product/<int:pk>/', UpdateProduct.as_view(), name = 'update_product'),
    path('delete_product/<int:pk>/', DeleteProduct.as_view(), name = 'delete_product'),
]   