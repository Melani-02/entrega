"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Proyecto1.views import saludo, hermana, hermano, mama, bienvenida  #importamos el modulo y el metodo
from familia.views import add_relative, list_family

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('hermano/', hermano),
    path('home/', bienvenida, name="bienvenida"),
    path('familia/', list_family, name="Lista Familiar"),
    path('add/', add_relative, name="add familiar"),
]
