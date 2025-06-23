from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('cart/', cart, name="cart"),
    path('explore/', explore, name="explore"),
    path('account/', account, name="account"),
    path('product/', product, name="product"),
]