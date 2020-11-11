from django.shortcuts import render
from .models import Transferencia

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def profile(request):
    return render(request, 'app/profile.html')

def transferencias(request):
    transferencias = Transferencia.objects.all()
    data = {
        'TRANSFERENCIAS' : transferencias
    }
    return render(request, 'app/transferencias.html', data)