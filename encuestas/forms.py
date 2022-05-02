from django import forms

from encuestas.models.alumnoCursoModel import alumnoCursoModel

from .models.encuestaSatisfaccionModel import encuestaSatisfaccionModel
from .models.preguntaSatisfaccionModel import preguntaSatisfaccionModel
from .models.encuestaCursoModel import encuestaCursoModel
from .models.preguntaCursoModel import preguntaCursoModel
from .models.cursoModel import cursoModel
from .models.alumnoModel import alumnoModel

class EncuestaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = encuestaSatisfaccionModel
        fields = '__all__'
        
class PreguntaSatisfaccionForm(forms.ModelForm):
    class Meta:
        model = preguntaSatisfaccionModel
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
        
        
    # opciones_1 = [('Deficiente','1'),('Malo','2'),('Regular','3')]
    # respuesta_1 = forms.ChoiceField(choices=opciones_1,widget=forms.RadioSelect(attrs={
    #     'type':'radio','class':'radio'
    # }))
    
