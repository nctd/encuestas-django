from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from encuestas.forms import empresaForm
from encuestas.models.alumnoCursoModel import alumnoCursoModel

from .models.userModel import User
from .models.preguntaSatisfaccionModel import preguntaSatisfaccionModel

from .models.encuestaSatisfaccionModel import encuestaSatisfaccionModel

from .models.empresaModel import empresaModel
from .models.cursoModel import cursoModel

from .models.alumnoModel import alumnoModel

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'first_name', 'last_name', 'is_staff',
        'es_empresa', 'es_alumno'
        )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('es_empresa', 'es_alumno')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Información personal', {
            'fields': ('first_name', 'last_name')
        }),
        ('Tipo de usuario', {
            'fields': ('es_empresa', 'es_alumno')
        })
    )


class empresaAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == "user":
            kwargs["queryset"] = User.objects.filter(es_empresa=True,es_alumno=False)
        return super(empresaAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(cursoModel)
admin.site.register(empresaModel,empresaAdmin)
admin.site.register(encuestaSatisfaccionModel)
admin.site.register(preguntaSatisfaccionModel)
admin.site.register(User, CustomUserAdmin)
admin.site.register(alumnoModel)
admin.site.register(alumnoCursoModel)