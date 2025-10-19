from hashlib import new
from django.shortcuts import redirect, render
from accounts.models import CustomUser
from accounts.forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
# Create your views here.


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, "خوش آمدید ")
                return redirect("home")
    return render(request, "accounts/login.html", {"form": form})


def register(request):
    form = RegisterForm
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.password = make_password(new_user.password)
            new_user.save()
            messages.success(request, "شما با موفقیت ثبت نام کردید")
            login(request, new_user)
            return redirect(
                "home",
            )
    return render(request, "accounts/register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")
