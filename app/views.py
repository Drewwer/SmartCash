from django.shortcuts import render
from .models import Transferencia
from .forms import formContacto

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

def contacto(request):
    data = {
        'form' : formContacto()
    }

    if request.method == 'POST':
        formulario = formContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Enviado"
        else:
            data["form"] = formulario

    return render(request, 'app/contacto.html', data)