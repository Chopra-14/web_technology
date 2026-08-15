from django.urls import path
from . import views

urlpatterns = [
    path('cotton_bhavan/', views.cotton_bhavan, name='cotton_bhavan'),
]