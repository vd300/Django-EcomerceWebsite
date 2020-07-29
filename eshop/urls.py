
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shopHome'),
    path('about/', views.about, name='About'),
    path('contact/', views.contact, name='Contact'),
    path('tracker/', views.tacker, name='TrackingStatus'),
    path('search/', views.search, name='Search'),
    path('productview/', views.productV, name='Productview'),
    path('checkout/', views.checkout, name='Checkout'),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("cart/", views.cart, name="cart"),
    path("wishlist/", views.wishlist, name="wishlist")
]
