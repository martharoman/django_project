from django.db import models

# Create your models here.
class Testimonios(models.Model):
    nombre = models.CharField(max_length=100)
    comentario = models.TextField()
    
    def __str__(self):
        return self.nombre

# segun el video, al crear el Model escribes el comando py manage.py makemigrations
# y te deberia de detectar esto que hiciste y despues escribes py manage.py maigrate
# instala la extension sqlite