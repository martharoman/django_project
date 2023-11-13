from django.http import HttpResponse

def index(request):
	return HttpResponse(
		"<center><h1>¡Hola mundo!</h1></center>"
		)
