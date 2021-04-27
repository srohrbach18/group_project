from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login',views.login),
    path('profile',views.profile),
    path('edit_user',views.edit_user),
    path('edit_card',views.edit_card),
    path('contact',views.contact),
    path('order', views.order),
    path('checkout', views.checkout),
    path('purchase', views.purchase),
]