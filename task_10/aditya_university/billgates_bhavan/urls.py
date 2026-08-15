from django.urls import path
from . import views

urlpatterns = [
    path('billgates_bhavan/', views.billgates_bhavan, name='billgates_bhavan'),
    path('bgbbhavan/details/<int:id>', views.details, name='details'),
]