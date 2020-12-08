import django_filters
from django_filters import DateFilter
from .models import Payment
from django.contrib.auth.models import User

#Filters go here
class PaymentFilter(django_filters.FilterSet):

    CHOICES = (
        ('latest','Latest'),
        ('recent','Recent')
    )

    ordering = django_filters.ChoiceFilter(
    label='Ordering',
    choices=CHOICES,
    method='filter_by_order',
    )
    start_date = DateFilter(field_name="time_posted", lookup_expr='gte')
    end_date = DateFilter(field_name="time_posted", lookup_expr='lte')

    class Meta:
        model = Payment
        fields = {
            'id': ['icontains'],
            'author__username': ['icontains'],
            'author__first_name': ['icontains']
        }

    def filter_by_order(self, queryset, time_posted, value):
        expression = 'time_posted' if value == 'Latest' else '-time_posted'
        return queryset.order_by(expression)
