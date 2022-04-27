from dataclasses import fields
from pyexpat import model
from django import forms

from .models import EncuestaSatisfaccion, PreguntaSatisfaccion

class EncuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = EncuestaSatisfaccion
        fields = '__all__'
        
class PreguntaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = PreguntaSatisfaccion
        fields = '__all__'    
        
        
        
    # opciones_1 = [('Deficiente','1'),('Malo','2'),('Regular','3')]
    # respuesta_1 = forms.ChoiceField(choices=opciones_1,widget=forms.RadioSelect(attrs={
    #     'type':'radio','class':'radio'
    # }))
    
