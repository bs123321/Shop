from django.shortcuts import render
from .models import Product, Order

def catalog(request):
    products = Product.objects.all()
    return render(request, 'shop/catalog.html', {'products': products})


def create_orders(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == "POST":
        u_address = request.POST["address"]
        u_email = request.POST["email"]
        u_phone = request.POST["phone"]
        u_count = request.POST["count"]
        u_koment = request.POST["koment"]
        Order.objects.create(
            product = Product.objects.get(id=product_id),
            address = u_address,
            email = u_email,
            count = u_count,
            phone = u_phone,
            koment = u_koment
        )
    return render(request, 'shop/create_orders.html')


def orders(request):
    orders = Order.objects.all()
    return render(request, 'shop/orders.html', {'orders': orders})


def product_detail(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'shop/product_detail.html', {'product': product})




# Create your views here.
