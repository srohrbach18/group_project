from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('order', views.order),
    path('checkout', views.checkout),
    path('purchase', views.purchase)
]