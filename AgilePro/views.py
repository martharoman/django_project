from django.shortcuts import render

def home(request):
	return render(request, 'AgilePro/home.html')

def login(request):
	return render(request, 'registration/login.html')

def agregar_testimonio(request):
	return render(request, 'AgilePro/testimonios/agregar.html')