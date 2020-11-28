from django.shortcuts import render


# Create your views here
def index(request):
    return render(request, 'financial/index.html')

def contrib_home(request):
    return render(request, 'financial/contrib_home.html')
