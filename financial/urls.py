from django.urls import path
from .views import (
    PaymentListView,
    CreatePayment,
    DeleteView,
    PaymentDetailView,
    PaymentUpdateView,
    InvoiceListView
)
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('invoice/', InvoiceListView.as_view(), name='invoice'),
    path('contrib_home/', PaymentListView.as_view(), name='contrib-home'),
    #path('contrib_home/', views.contrib_home, name='contrib_home'),
    path('contrib_home/delete/(?P<pk>[0-9]+)$', DeleteView.as_view(), name='delete-view'),
    path('contrib_home/detail/<uuid:pk>', PaymentDetailView.as_view(), name='payment-detail'),
    path('contrib_home/<uuid:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('contrib_home/new/', CreatePayment.as_view(), name='payment-create'),
    path(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.update_status, name='update-status')
]
