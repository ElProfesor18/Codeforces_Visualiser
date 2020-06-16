from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    path('', views.compare, name='compare'),
    path('<str:handles>', views.compute, name='compute'),
]

