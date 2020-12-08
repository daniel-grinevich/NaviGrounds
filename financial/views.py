from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.views.generic import (
        ListView,
        CreateView,
        DeleteView
)
from .models import Payment
from .filters import PaymentFilter


# Create your views here
def index(request):
    return render(request, 'financial/index.html')

class PaymentListView(LoginRequiredMixin, ListView):

    model = Payment
    template_name = 'financial/contrib_home.html'
    context_object_name = 'payments'
    ordering = ['-time_posted']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PaymentFilter(self.request.GET, queryset=self.get_queryset())
        return context


class CreatePayment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Payment
    fields = ['amount']

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(
            self.request,
            f'{form.instance.author.first_name} successfully added payment, the hex code is: {form.instance.id}'
        )
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
            #amount = form.cleaned_data['amount']

class DeleteView(SuccessMessageMixin, DeleteView):
    model = Payment
    success_url = '/financial/contrib_home'

    def delete(self,request, *args, **kwargs):
        messages.success(
            self.request,
            f'Successfully deleted payment'
        )
        self.object = self.get_object()
        super(DeleteView, self).delete(request, *args, **kwargs)
        return HttpResponseRedirect(self.get_success_url())
        #form = PaymentCreateForm()
        #return render(request, 'financial/payment_form.html', {'form': form})
