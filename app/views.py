from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def profile(request):
    return render(request, 'app/profile.html')
