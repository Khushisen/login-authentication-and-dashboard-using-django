from django.urls import path
from . import views

urlpatterns = [
    path("services/",views.services,name='services'),
    path('book/',views.book,name='book'),
    path('products/',views.product_list,name='product_list'),
    path('products/<int:product_id>/',views.product_detail,name='product_detail'),
    path('cart/add/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.cart_detail,name='cart_detail'),
    path('checkout/',views.checkout,name='checkout'),

]
