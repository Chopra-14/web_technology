from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.form,
        name='register'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'admin-dashboard/',
        views.admin_dashboard,
        name='admin_dashboard'
    ),

    path(
        'user-dashboard/',
        views.user_dashboard,
        name='user_dashboard'
    ),

    path(
        'edit-product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),

    path(
        'buy-product/<int:product_id>/',
        views.buy_product,
        name='buy_product'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

]