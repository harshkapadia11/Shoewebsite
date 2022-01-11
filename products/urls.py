from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('home/', views.home),
    path('home/brand/', views.brand),
    path('home/credits/', views.credits, name="credits"),
    path('home/profile/', views.profile, name="profile"),
    path('home/brand/address/', views.address, name="address"),
    path('home/order/', views.order, name="order"),
    path('home/logout/', views.logout, name="logout"),
    path('home/products/', views.products, name="products")
]