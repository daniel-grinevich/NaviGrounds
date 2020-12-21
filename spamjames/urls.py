from django.urls import path
from . import views

urlpatterns = [
    path('spamjames/', views.sms, name='sms'),
]
