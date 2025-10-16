from django.shortcuts import redirect, render
from accounts.models import CustomUser
from accounts.forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
# Create your views here.


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = CustomUser.objects.filter(username=username).first()
            if check_password(password, user.password):
                login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html", {"form": form})
