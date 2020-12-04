from django.urls import path
from .views import (
    PaymentListView,
    CreatePayment
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contrib_home/', PaymentListView.as_view(), name='contrib-home'),
    #path('contrib_home/', views.contrib_home, name='contrib_home'),
    path('contrib_home/new/', CreatePayment.as_view(), name='payment-create')
]
