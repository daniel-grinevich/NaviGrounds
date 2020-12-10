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
        DeleteView,
        DetailView,
        UpdateView
)
from .models import Payment, Category
from .filters import PaymentFilter


# Create your views here
def index(request):
    return render(request, 'financial/index.html')

class PaymentListView(LoginRequiredMixin, ListView):

    model = Payment
    template_name = 'financial/contrib_home.html'
    context_object_name = 'payments'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get('latest'):
            queryset = Payment.objects.order_by('time_posted')
            return queryset
        if self.request.GET.get('earliest'):
            queryset = Payment.objects.order_by('-time_posted')
            return queryset
        if self.request.GET.get('greatest'):
            queryset = Payment.objects.order_by('-amount')
            return queryset
        if self.request.GET.get('smallest'):
            queryset = Payment.objects.order_by('amount')
            return queryset
        if self.request.GET.get('contribution'):
            queryset = Payment.objects.filter(type__name='Contribution').order_by('-time_posted')
            return queryset
        if self.request.GET.get('expense'):
            queryset = Payment.objects.filter(type__name='Expense')
            return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PaymentFilter(self.request.GET, queryset=self.get_queryset())
        return context

class CreatePayment(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Payment
    fields = ['amount','type']

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

class PaymentDetailView(DetailView):
    model = Payment

class PaymentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Payment
    fields = ['amount','type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
