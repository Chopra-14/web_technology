from django.urls import path
from . import views

urlpatterns = [
    path('kl_rao_bhavan/', views.kl_rao_bhavan, name='kl_rao_bhavan'),
]