from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.search, name='search'),
    path('<str:handle>', views.show, name='show'),
    path('time_table/', views.time_table, name='timetable'),
] 
  