from django.shortcuts import render
from .models import Testimonios
from .forms import TestimoniosAgregar

def home(request):
    testimonios = Testimonios.objects.all()

    return render(request, 'AgilePro/home.html', {'testimonios': testimonios})

def login(request):
	return render(request, 'registration/login.html')


def agregar_testimonio(request):

    data = {
         'form': TestimoniosAgregar()
    }

    return render(request, 'AgilePro/testimonios/agregar.html', data)