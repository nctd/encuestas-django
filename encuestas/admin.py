from django.contrib import admin

from .models.preguntaSatisfaccionModel import preguntaSatisfaccionModel

from .models.encuestaSatisfaccionModel import encuestaSatisfaccionModel

from .models.empresaModel import empresaModel
from .models.cursoModel import cursoModel

admin.site.register(cursoModel)
admin.site.register(empresaModel)
admin.site.register(encuestaSatisfaccionModel)
admin.site.register(preguntaSatisfaccionModel)