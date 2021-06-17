from django.urls import path
from . import views
from .views import (
    CreatePayment
)


urlpatterns = [
    path('', views.store, name="store"),
    path('customize/', views.customize, name="customize"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update-item"),
    path('add/', CreatePayment.as_view(), name='product-add'),
    path('process_order/', views.processOrder, name="process-order ")
]
