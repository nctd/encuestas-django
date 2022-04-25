from dataclasses import fields
from django import forms

from .models import EncuestaSatisfaccion

class EncuestaSatisfaccionForm(forms.Form):
    
    opciones_1 = [('A1','Nisi officia'),('iusmod minim','excepteur do consequat'),('Z3','ipsum deserunt nostrud')]
    respuesta_1 = forms.ChoiceField(choices=opciones_1,widget=forms.RadioSelect)
