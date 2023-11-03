from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from . forms import UserRegistrationForm,UserLoginForm
from django.contrib import messages
from . models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout, authenticate

# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('shop:all_products')
            else:
                messages.error(request, "Invalid credentials")

        except Exception as e:
            messages.error(request, f"Authentication failed: {e}")
            return redirect('accounts:home')

        else:
            return redirect('accounts:home')
    return render(request,'home.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            messages.error(request, "! Password missmatch.")
            return redirect("accounts:register")
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect("accounts:home")
        except IntegrityError:
            messages.error(request, "! username or email exists")
            return redirect("accounts:register")

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:home')

    



