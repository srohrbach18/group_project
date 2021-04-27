from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login',views.login),
    path('profile',views.profile),
    path('edit_user',views.edit_user),
    path('contact',views.contact),
    path('menu', views.menu),
    path('add_food',views.add_food),
]