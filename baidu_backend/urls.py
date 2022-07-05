"""baidu_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from backend_api import views

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/detect_change', views.detect_change),
    path('api/extract_object', views.extract_object),
    path('api/detect_object', views.detect_object),
    path('api/classify_pixel', views.classify_pixel)
]
