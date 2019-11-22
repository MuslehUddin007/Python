from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.user_login, name='user_login'),
    path('send',views.send, name='send'),
    path('success',views.success, name='success'),
    path('check',views.check, name='check')
]