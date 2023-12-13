from django import forms
from .models import Testimonios

#agrgar testimonios
class TestimoniosAgregar(forms.ModelForm):
    class Meta:
        model = Testimonios
        fields = '__all__'