from django.shortcuts import render, get_object_or_404, redirect
from .models import Testimonios
from .forms import TestimoniosAgregar

def index(request):
    testimonios = Testimonios.objects.all()

    return render(request, 'AgilePro/index.html', {'testimonios': testimonios})

def home(request):
    testimonios = Testimonios.objects.all()

    return render(request, 'AgilePro/home.html', {'testimonios': testimonios})

def login(request):
	return render(request, 'registration/login.html')


def listado_testimonios(request):
     
    testimonios = Testimonios.objects.all()
    data = {
         'testimonios': testimonios
    }

    return render(request, 'AgilePro/testimonios/listado.html', data)

def agregar_testimonio(request):

    data = {
         'form': TestimoniosAgregar()
    }

    if request.method == 'POST':
        formulario = TestimoniosAgregar(data=request.POST)
        if formulario.is_valid():
              formulario.save()
              data['mensaje'] = "¡Enviado Correctamente!"
        else:
             data['form'] = formulario

    return render(request, 'AgilePro/testimonios/agregar.html', data)


def editar_testimonio(request, id):
    
    testimonios = get_object_or_404(Testimonios, id=id)

    data = {
        'form': TestimoniosAgregar(instance=testimonios)
    }

    #para que la edición del testimonio funcione
    if request.method == 'POST':
        formulario = TestimoniosAgregar(data=request.POST, instance=testimonios)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "¡Testimonio Modificado con Éxito!"
            return redirect(to='listado_testimonios')
        data['form'] = formulario

    return render(request, 'AgilePro/testimonios/editar.html', data)

def eliminar_testimonio(request, id):

    testimonio = get_object_or_404(Testimonios, id=id)
    testimonio.delete()
    return redirect(to='listado_testimonios')