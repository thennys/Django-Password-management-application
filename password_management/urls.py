"""
URL configuration for password_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from password_entry import views


urlpatterns = [
    path('', views.password_list, name='password_list'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


    path('passwords/', views.password_list, name='password_list'),
    path('passwords/add/', views.password_create, name='password_create'),
    path('passwords/<int:pk>/', views.password_detail, name='password_detail'),
    path('passwords/<int:pk>/edit/', views.password_update, name='password_update'),
    path('passwords/<int:pk>/delete/', views.password_delete, name='password_delete'),
    

]
