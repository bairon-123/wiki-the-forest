from django.contrib import admin
from .models import Usuario, RolUsuario  # Solo importa los modelos que existen

admin.site.register(Usuario)
admin.site.register(RolUsuario)