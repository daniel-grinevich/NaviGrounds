from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contrib_home/', views.contrib_home, name='contrib_home')
]
