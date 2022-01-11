from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Brand, Order
from django.contrib import sessions
from django.contrib.auth.models import User
import datetime as date


# Creaddate your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse('New Products')


def home(request):
    if check_session(request):
        username = request.session['username']
        brands = Brand.objects.all()

        return render(request, 'home.html', {'brands': brands, 'username': username})

    else:
        return redirect('/register/login/')


def brand(request):
    if check_session(request):
        name = request.GET['b']
        product_brand = Product.objects.filter(brand=name)
        return render(request, 'category.html', {'category': name, 'Products': product_brand})
    else:
        return redirect('/register/login/')


def products(request):
    if check_session(request):
        product = Product.objects.all()
        return render(request, 'products.html', {'products':product})
    else:
        return redirect('/register/login/')


def credits(request):
    if check_session(request):
        return render(request, 'credits.html')
    else:
        return redirect('/register/login/')


def profile(request):
    if check_session(request):
        if request.user.is_authenticated:
            return render(request, 'profile.html')
        else:
            return redirect('/register/login/')
    else:
        return redirect('/register/login/')


def address(request):
    if check_session(request):

        if request.method == 'POST':
            shoe_id = request.POST['shoe_id']
            user_id = request.POST['user_name']
            shoe_name = request.POST['shoe_name']
            price = request.POST['amount']
            add = request.POST['address']
            ordered_On = date.date.today()
            shoe = Product.objects.get(id=shoe_id)
            shoe.stock -= 1
            shoe.save()
            order1 = Order(shoe_name=shoe_name, shoe_id=shoe_id, user_id=user_id, address=add, amount=price,
                           order_date=ordered_On)
            order1.save()
            return redirect('/products/home/')
        username = request.session['username']
        shoe_id = request.GET['id']
        shoe = Product.objects.filter(id=shoe_id)
        return render(request, 'address.html', {'username': username, 'id': shoe})
    else:
        return redirect('/register/login/')


def check_session(request):
    username = request.session['username']
    if username:
        return True
    else:
        return False


class OrderDetails:
    def __init__(self,order,img):
        self.img = img
        self.order = order


def order(request):
    if check_session(request):
        username = request.session['username']
        order1 = Order.objects.filter(user_id=username)
        orders = []
        for order2 in order1:
            shoe = Product.objects.get(id=order2.shoe_id)
            item = OrderDetails(order2,shoe.image_url)
            orders.append(item)
        return render(request, 'order.html', {'orders': orders})
    else:
        return redirect('/register/login/')


def logout(request):
    request.session['username'] = None
    return redirect('/register/login/')