from django.shortcuts import render
from .models import *

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'store/Store.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer=request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False) # To study
        items = order.orderitem_set.all() # To study
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0} # for unauthenticated user

    context = {'items':items, 'order':order}
    return render(request, 'store/Cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/Checkout.html', context)


