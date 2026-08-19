from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm


def home(request):
    return render(request, "home.html")


def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]

            return redirect("/login/")

    else:
        form = SignupForm()

    return render(request, "signup.html", {"form": form})


def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]

            return render(request, "home.html", {
                "username": username
            })

    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})