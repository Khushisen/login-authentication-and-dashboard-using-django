from django.shortcuts import render,get_object_or_404,redirect
from .models import Product
from .cart import Cart

def services(request):
    return render(request,'services.html')
def book(request):
    return render(request,'book.html')

def product_list(request):
    products = Product.objects.all()
    return render(request,'product_list.html',{'products': products})

def product_detail(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    return render(request,'product_detail.html',{'product':product})

def add_to_cart(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart(request)
    cart.add(product=product,quantity=int(request.POST.get('quantity')))
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request,'card_detail.html',{'cart':cart})

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        #handle order processing
        #integrate payment here
        #redirect to order confirmation
        pass
    return render(request,'checkout.html',{'cart': cart})