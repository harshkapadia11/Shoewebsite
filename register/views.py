from django.shortcuts import render, redirect
from django.contrib import messages, sessions
from django.contrib.auth.models import User, auth

# Create your views here.


def login(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            request.session['username'] = username
            return redirect("/products/home/")
        else:
            messages.info(request,'invalid-credentials')
            return redirect('/register/login/')

    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.info(request, 'Password Mismatch')
            return redirect('/register/register/')
        else:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists!!!')
                return redirect('/register/register/')
            else:
                user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.info(request, 'User Created')
                return redirect('/register/login/')

    else:
        return render(request, 'register.html')





