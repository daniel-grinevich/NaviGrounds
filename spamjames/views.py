from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from twilio.rest import Client
from django.contrib import messages
from .forms import SpamJamesForm

# Create your views here.
def sms(request):
    if request.method == 'POST':
        spam_form = SpamJamesForm(request.POST)
        if spam_form.is_valid():
            sms = spam_form.cleaned_data['sms']
            client = Client("ACe7f8c5831f763a6ba8a76d34c6c20a34", "b170bcd59a836fc6805b0607a5b22424")
            client.messages.create(
                                to="+12567625466",
                                from_="+18049132947",
                                body=sms
                                    )
            messages.success(request, f'MSG sent to James Ridgeway')
            return redirect('sms')

    return render(request, 'spamjames/sms.html')
