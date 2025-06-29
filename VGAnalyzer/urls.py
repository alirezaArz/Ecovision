"""
URL configuration for VGAnalyzer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', views.admin_panel_view, name='admin_panel'),
    path('admin/control/', views.control_view, name='control_commands'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('crypto/', views.get_crypto_data, name='crypto_data'),
    path('news/', views.get_main_news, name='news_data'),
    path('api/<str:id>/',views.api_nav, name = 'api_nav'),
]
