from django.urls import path
from . import views

urlpatterns = [
    path('rtb_bhavan/', views.rtb_bhavan, name='rtb_bhavan'),
]