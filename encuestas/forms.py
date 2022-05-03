from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models.respuestaSatisfaccionModel import respuestaSatisfaccionModel
from .models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from .models.encuestaCursoModel import encuestaCursoModel
from .models.alumnoModel import alumnoModel
from .models.preguntaCursoModel import preguntaCursoModel
from .models.alumnoCursoModel import alumnoCursoModel
from .models.cursoModel import cursoModel

class EncuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = encuestaSatisfaccionModel
        fields = '__all__'
        
class RespuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = respuestaSatisfaccionModel
        fields = '__all__'    
        
class cursoEncuestaForm(forms.ModelForm):
    class Meta:
        model = encuestaCursoModel
        fields = '__all__'
        
class cursoForm(forms.ModelForm):
    class Meta:
        model = cursoModel
        fields = '__all__'    
        
class alumnoForm(forms.ModelForm):
    class Meta:
        model = alumnoModel
        fields = '__all__'    
        
class EncuestaCursoForm(forms.ModelForm):
    class Meta:
        model = encuestaCursoModel
        fields = '__all__'
        
class PreguntaCursoForm(forms.ModelForm):
    class Meta:
        model = preguntaCursoModel
        fields = '__all__'    

class alumnoCursoForm(forms.ModelForm):
    class Meta:
        model = alumnoCursoModel
        fields = '__all__'    
        
    
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password','id':'password1'}),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password','id':'password2'}),
    )
    first_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control','type': 'text','id':'first_name'}))
    last_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control','type': 'text','id':'last_name'})) 


    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1',
            'password2'
        ]
        widgets = {
            'username':
                forms.TextInput(attrs={
                    'class': 'form-control',
                    'type': 'text',
                    'id':'username'
                },),
            'email':
                forms.TextInput(attrs={
                    'class': 'form-control',
                    'type': 'email',
                    'id':'email',
                },),
                            
        }
