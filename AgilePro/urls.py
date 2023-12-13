from django.urls import path
from .views import home, login, agregar_testimonio

urlpatterns = [
	path('', home, name='home'),
 	path('login/', login, name='login'),
	path('agregar-testimonio/', agregar_testimonio, name='agregar_testimonio'),
]