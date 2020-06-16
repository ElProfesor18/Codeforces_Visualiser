from django.conf.urls import url, include
from django.urls import path
from login import views

# SET THE NAMESPACE!
app_name = 'login'

urlpatterns=[
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login, name='user_login'),
]