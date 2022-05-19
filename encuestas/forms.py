from django import forms

from django.contrib.auth.forms import UserCreationForm

from encuestas.models.empresaModel import empresaModel
from encuestas.models.respuestaAlumnoModel import respuestaAlumnoModel
from encuestas.models.respuestaRecepcionServicioModel import respuestaRecepcionServicioModel
# from django.contrib.auth.models import User
from .models.userModel import User

from .models.respuestaSatisfaccionModel import respuestaSatisfaccionModel
from .models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from .models.encuestaAlumnoModel import encuestaAlumnoModel
from .models.alumnoModel import alumnoModel
from .models.preguntaAlumnoModel import preguntaAlumnoModel
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
        
class cursoForm(forms.ModelForm):
    class Meta:
        model = cursoModel
        fields = '__all__'    
        
class alumnoForm(forms.ModelForm):
    class Meta:
        model = alumnoModel
        fields = '__all__'    
        
class EncuestaAlumnoForm(forms.ModelForm):
    class Meta:
        model = encuestaAlumnoModel
        fields = '__all__'
        
class PreguntaAlumnoForm(forms.ModelForm):
    class Meta:
        model = preguntaAlumnoModel
        fields = '__all__'    

class RespuestaAlumnoForm(forms.ModelForm):
    class Meta:
        model = respuestaAlumnoModel
        fields = '__all__'  

class alumnoCursoForm(forms.ModelForm):
    class Meta:
        model = alumnoCursoModel
        fields = '__all__'    
        
class empresaForm(forms.ModelForm):
    
    class Meta:
        model = empresaModel
        fields = '__all__'
        
class RespuestaRecepcionServicioForm(forms.ModelForm):
    class Meta:
        model = respuestaRecepcionServicioModel
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
            'password2','es_empresa','es_alumno'
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


class preguntaRecepcionServicioInLineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        total_porcentaje = sum(f.cleaned_data.get('porcentaje') for f in self.forms)
        if total_porcentaje != 100:
            raise forms.ValidationError("La suma de los porcentajes debe ser 100")