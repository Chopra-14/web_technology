from django.urls import path
from . import views

urlpatterns = [
    path('baskara_bhavan/', views.baskara_bhavan, name='baskara_bhavan'),
]