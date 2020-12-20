from django import forms


class SpamJamesForm(forms.Form):
    sms = forms.CharField(max_length=200)
