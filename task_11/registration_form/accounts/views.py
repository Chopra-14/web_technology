from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


def signup(request):
    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password == confirm_password:

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            user.save()

            return render(request, "home.html", {
                "username": username
            })

        else:
            error_message = "Passwords do not match."

            return render(request, "signup.html", {
                "error_message": error_message
            })

    return render(request, "signup.html")


def login_view(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return render(request, "home.html", {
                "username": username
            })

        else:
            error_message = "Invalid username or password."

            return render(request, "login.html", {
                "error_message": error_message
            })

    return render(request, "login.html")