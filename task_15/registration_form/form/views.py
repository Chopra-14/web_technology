from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import (
    RegistrationForm,
    LoginForm,
    ProductForm,
    PurchaseForm
)

from .models import Product, Purchase, Profile


# -------------------------
# Registration
# -------------------------

def form(request):

    if request.method == 'POST':

        registration_form = RegistrationForm(request.POST)

        if registration_form.is_valid():

            user = registration_form.save()

            Profile.objects.create(
                user=user,
                role=registration_form.cleaned_data['role']
            )

            login(request, user)

            if registration_form.cleaned_data['role'] == 'admin':
                return redirect('admin_dashboard')

            return redirect('user_dashboard')

    else:

        registration_form = RegistrationForm()

    return render(
        request,
        'register.html',
        {
            'form': registration_form
        }
    )


# -------------------------
# Login
# -------------------------

def login_view(request):

    if request.method == 'POST':

        login_form = LoginForm(request.POST)

        if login_form.is_valid():

            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:

                login(request, user)

                if user.profile.role == 'admin':
                    return redirect('admin_dashboard')

                return redirect('user_dashboard')

            login_form.add_error(
                None,
                'Invalid email or password.'
            )

    else:

        login_form = LoginForm()

    return render(
        request,
        'login.html',
        {
            'form': login_form
        }
    )


# -------------------------
# Admin Dashboard
# -------------------------

@login_required
def admin_dashboard(request):

    if request.user.profile.role != 'admin':
        return redirect('user_dashboard')

    products = Product.objects.all()

    if request.method == 'POST':

        product_form = ProductForm(request.POST)

        if product_form.is_valid():

            product_form.save()

            return redirect('admin_dashboard')

    else:

        product_form = ProductForm()

    return render(
        request,
        'admin_dashboard.html',
        {
            'form': product_form,
            'products': products
        }
    )


# -------------------------
# Edit Product
# -------------------------

@login_required
def edit_product(request, product_id):

    if request.user.profile.role != 'admin':
        return redirect('user_dashboard')

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == 'POST':

        product_form = ProductForm(
            request.POST,
            instance=product
        )

        if product_form.is_valid():

            product_form.save()

            return redirect('admin_dashboard')

    else:

        product_form = ProductForm(
            instance=product
        )

    return render(
        request,
        'edit_product.html',
        {
            'form': product_form,
            'product': product
        }
    )


# -------------------------
# Delete Product
# -------------------------

@login_required
def delete_product(request, product_id):

    if request.user.profile.role != 'admin':
        return redirect('user_dashboard')

    product = get_object_or_404(
        Product,
        id=product_id
    )

    product.delete()

    return redirect('admin_dashboard')


# -------------------------
# User Dashboard
# -------------------------

@login_required
def user_dashboard(request):

    products = Product.objects.all()

    return render(
        request,
        'user_dashboard.html',
        {
            'products': products
        }
    )


# -------------------------
# Buy Product
# -------------------------

@login_required
def buy_product(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    if request.method == 'POST':

        purchase_form = PurchaseForm(request.POST)

        if purchase_form.is_valid():

            purchase_quantity = (
                purchase_form.cleaned_data['quantity']
            )

            if purchase_quantity <= product.quantity:

                Purchase.objects.create(
                    user=request.user,
                    product=product,
                    quantity=purchase_quantity
                )

                product.quantity -= purchase_quantity
                product.save()

                return redirect('user_dashboard')

            purchase_form.add_error(
                'quantity',
                'Not enough stock available.'
            )

    else:

        purchase_form = PurchaseForm()

    return render(
        request,
        'buy_product.html',
        {
            'form': purchase_form,
            'product': product
        }
    )


# -------------------------
# Logout
# -------------------------

def logout_view(request):

    logout(request)

    return redirect('login')