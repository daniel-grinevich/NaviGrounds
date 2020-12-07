import django_filters
from .models import Payment
from django.contrib.auth.models import User

#Filters go here
class PaymentFilter(django_filters.FilterSet):

    class Meta:
        model = Payment
        fields = {
            'time_posted': ['contains'],
            'author__username': ['contains']
        }
