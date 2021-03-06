from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from login import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('search/', include('visualise.urls')),

    path('compare/', include('compare.urls')),

    path('contact_us/', views.contact_us, name='contact'),

    path('', views.index, name='index'),
    path('login/', include('login.urls')),
    path('logout/', views.user_logout, name='logout'),
]