from django.urls import path
from . import views
urlpatterns = [
    path('',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('checkout_success/',views.checkout_success,name='checkout_success'),
    path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('remove/<int:product_id>/', views.remove, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', views.remove_cart_item, name='remove_cart_item'),
]