from django.shortcuts import render
from .models import Testimonios

def home(request):
    testimonios = Testimonios.objects.all()

    return render(request, 'AgilePro/home.html', {'testimonios': testimonios})

def login(request):
	return render(request, 'registration/login.html')

def agregar_testimonio(request):
	return render(request, 'AgilePro/testimonios/agregar.html')