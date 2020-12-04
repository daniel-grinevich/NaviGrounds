from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        CreateView
)
from .models import Payment
from .forms import PaymentCreateForm

# Create your views here
def index(request):
    return render(request, 'financial/index.html')

class PaymentListView(ListView):
    model = Payment
    template_name = 'financial/contrib_home.html'
    context_object_name = 'payments'


class CreatePayment(LoginRequiredMixin, CreateView):
    model = Payment
    fields = ['amount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
            #amount = form.cleaned_data['amount']


    #form = PaymentCreateForm()
    #return render(request, 'financial/payment_form.html', {'form': form})
