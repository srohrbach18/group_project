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
    path('handle_add_food',views.handle_add_food),
    path('edit_item/<int:item_id>',views.edit_item),
    path('handle_edit_item/<int:item_id>',views.handle_edit_item),
    path('handle_login',views.handle_login),
    path('admin',views.admin),
    path('logout',views.logout),
    path('delete_food/<int:item_id>',views.delete_food),

]