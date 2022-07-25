from django.contrib import admin
from django.urls import path,include
from .views import home,hacked

urlpatterns = [
    path('',home,name="home-page"),
    path('hacked/',hacked,name="hacked-page")
]
