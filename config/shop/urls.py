from django.urls import path
from shop.views import *

urlpatterns = [
    path('', catalog),
    path('create_orders/<int:product_id>/', create_orders, name = "create_order"),
    path('orders/', orders),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
]
