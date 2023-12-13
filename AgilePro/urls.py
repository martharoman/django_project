from django.urls import path
from .views import index, home, login, listado_testimonios, agregar_testimonio, editar_testimonio, eliminar_testimonio

urlpatterns = [
	path('', index, name='index'),
    path('home/', home, name='home'),
 	path('login/', login, name='login'),
    path('listado-testimonios/', listado_testimonios, name='listado_testimonios'),
	path('agregar-testimonio/', agregar_testimonio, name='agregar_testimonio'),
    path('editar-testimonio/<id>/', editar_testimonio, name='editar_testimonio'),
    path('eliminar-testimonio/<id>', eliminar_testimonio, name='eliminar_testimonio'),
]