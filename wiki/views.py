from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from .models import Usuario, RolUsuario
from django.contrib import messages
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import RolUsuario 


def animales(request):
    return render(request, 'wiki/Animales.html')

def armas(request):
    return render(request, 'wiki/Armas.html')

def construcciones(request):
    return render(request, 'wiki/Construcciones.html')

def consumibles(request):
    return render(request, 'wiki/Consumibles.html')

def enemigos(request):
    return render(request, 'wiki/Enemigos.html')

def flora(request):
    return render(request, 'wiki/Flora.html')

def forowiki(request):
    return render(request, 'wiki/forowiki.html')

def historia(request):
    return render(request, 'wiki/historia.html')

def logros(request):
    return render(request, 'wiki/Logros.html')

def lugarestf(request):
    return render(request, 'wiki/Lugarestf.html')

def menuprincipal_wiki(request):
    return render(request, 'wiki/menuprincipal_wiki.html')

def recuperarcontra(request):
    return render(request, 'wiki/recuperarcontra.html')

def editar_informacion(request):
    return render(request, 'wiki/editar_informacion.html')




# Vista mi cuenta con edición de perfil, contraseña y eliminación de cuenta

def micuentatf(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        messages.error(request, "Debes iniciar sesión primero.")
        return redirect('inicio_sesion_wiki')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        messages.error(request, "El usuario no existe.")
        return redirect('inicio_sesion_wiki')

    if request.method == 'POST':
        if 'guardar' in request.POST:
            nuevo_email = request.POST.get('email')
            nueva_password = request.POST.get('password')

            if not nuevo_email:
                messages.error(request, 'El correo es obligatorio.')
                return redirect('micuentatf')

            if Usuario.objects.exclude(pk=usuario.pk).filter(email=nuevo_email).exists():
                messages.error(request, 'El correo ya está registrado.')
                return redirect('micuentatf')

            usuario.email = nuevo_email

            if nueva_password:
                usuario.password = nueva_password  # Si usas encriptación, aquí debería ir `make_password(nueva_password)`

            usuario.save()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('micuentatf')

        elif 'eliminar' in request.POST:
            usuario.delete()
            request.session.flush()
            messages.success(request, 'Cuenta eliminada. Debes registrarte nuevamente.')
            return redirect('registrase_wiki')

    return render(request, 'wiki/micuentatf.html', {'usuario': usuario})

def cerrar_sesion(request):
    logout(request)  
    messages.success(request, "Has cerrado sesión con éxito.")
    return redirect('inicio_sesion_wiki')  


@login_required(login_url='inicio_sesion_wiki')
def editar_informacion(request):
    usuario = request.user

    if request.method == 'POST':
        nuevo_email = request.POST.get('email')
        nueva_password = request.POST.get('password')

        if not nuevo_email:
            messages.error(request, 'El correo es obligatorio.')
            return redirect('editar_informacion')

        if Usuario.objects.exclude(pk=usuario.pk).filter(email=nuevo_email).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('editar_informacion')

        usuario.email = nuevo_email
        if nueva_password:
            usuario.password = nueva_password
            update_session_auth_hash(request, usuario)

        usuario.save()
        messages.success(request, 'Información actualizada.')
        return redirect('micuentatf')

    return render(request, 'wiki/editar_informacion.html', {'usuario': usuario})

def panel_administrador(request):
    usuario_id = request.session.get('usuario_id')

    if not usuario_id:
        return redirect('inicio_sesion_wiki')

    usuario = Usuario.objects.get(id=usuario_id)

    # Solo permitir acceso a administradores
    if usuario.rol.nombre != 'Administrador':
        return HttpResponseForbidden("Acceso denegado. No tienes permisos para ver esta página.")

    usuarios = Usuario.objects.all()
    return render(request, 'wiki/panel_administrador.html', {'usuarios': usuarios})

# Vista de inicio de sesión
class SimpleBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(email=username)
            if user.password == password:
                return user
        except Usuario.DoesNotExist:
            return None
        return None

def inicio_sesion_wiki(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')

        try:
            usuario = Usuario.objects.get(email=email)
            if usuario.password == password:  # ← sin encriptado
                request.session['usuario_id'] = usuario.id

                # 🔁 Si existe el parámetro 'next', redirige allí. Si no, va a 'micuentatf'
                next_url = request.GET.get('next', 'micuentatf')
                return redirect(next_url)
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo no registrado.')

    return render(request, 'wiki/inicio_sesion_wiki.html')


# Vista de registro
def registrase_wiki(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if not email or not password1 or not password2:
            messages.error(request, 'Todos los campos son obligatorios.')
            return redirect('registrase_wiki')

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registrase_wiki')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El correo ya está registrado.')
            return redirect('registrase_wiki')

        rol_default, _ = RolUsuario.objects.get_or_create(nombre='Usuario')
        nuevo_usuario = Usuario(email=email, password=password1, rol=rol_default)  # password sin hash
        nuevo_usuario.save()

        messages.success(request, '¡Usuario registrado con éxito! Ahora puedes iniciar sesión.')
        return redirect('inicio_sesion_wiki')

    return render(request, 'wiki/registrase_wiki.html')

@login_required(login_url='inicio_sesion_wiki')
def editar_usuario(request, id):
    if request.user.rol.nombre != 'Administrador':
        return HttpResponseForbidden("No tienes permiso para editar usuarios.")
    
    usuario = get_object_or_404(Usuario, id=id)
    roles = RolUsuario.objects.all()

    if request.method == 'POST':
        usuario.email = request.POST.get('email')
        usuario.is_active = 'is_active' in request.POST
        nuevo_rol_id = request.POST.get('rol')
        if nuevo_rol_id:
            usuario.rol = get_object_or_404(RolUsuario, id=nuevo_rol_id)
        usuario.save()
        messages.success(request, 'Usuario editado correctamente.')
        return redirect('panel_administrador')

    return render(request, 'wiki/editar_usuario.html', {'usuario': usuario, 'roles': roles})

@login_required(login_url='inicio_sesion_wiki')
def panel_administrador(request):
    if request.user.rol.nombre != 'Administrador':
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    usuarios = Usuario.objects.all()
    return render(request, 'wiki/panel_administrador.html', {'usuarios': usuarios})

@login_required(login_url='inicio_sesion_wiki')
def eliminar_usuario(request, id):
    if request.user.rol.nombre != 'Administrador':
        return HttpResponseForbidden("No tienes permiso para eliminar usuarios.")
    
    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('panel_administrador')

    return render(request, 'wiki/confirmar_eliminar.html', {'usuario': usuario})

def menuprincipal_wiki(request):
    usuario_id = request.session.get('usuario_id')
    usuario_actual = None

    if usuario_id:
        try:
            usuario_actual = Usuario.objects.get(id=usuario_id)
        except Usuario.DoesNotExist:
            pass

    return render(request, 'wiki/menuprincipal_wiki.html', {'usuario_actual': usuario_actual})

def panel_administrador_redirect(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('inicio_sesion_wiki')

    try:
        usuario = Usuario.objects.get(id=usuario_id)
    except Usuario.DoesNotExist:
        return redirect('inicio_sesion_wiki')

    if usuario.rol.nombre == 'Administrador':
        return redirect('panel_administrador')
    else:
        messages.error(request, "No tienes permisos para acceder al panel de administrador.")
        return redirect('menuprincipal_wiki')