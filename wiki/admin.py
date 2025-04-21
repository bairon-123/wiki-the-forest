from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Arma, Usuario, RolUsuario, Animal


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ('email', 'rol', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'rol')
    ordering = ('email',)
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Información personal'), {'fields': ('rol',)}),
        (_('Permisos'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Fechas importantes'), {'fields': ('last_login',)}),
    )


@admin.register(RolUsuario)
class RolUsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ( 'nombre', 'hostilidad', 'descripcion', 'imagen_preview')
    search_fields = ('numero', 'nombre', 'hostilidad')
    list_filter = ('hostilidad',)

    def imagen_preview(self, obj):
        return obj.imagen.url if obj.imagen else "-"
    imagen_preview.short_description = "Imagen"

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
@admin.register(Arma)
class ArmaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre', 'tipo')
    search_fields = ('nombre', 'tipo')