from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Arma, Usuario, RolUsuario, Animal

def animales(request):
    animales_list = Animal.objects.all().order_by('numero')
    paginator = Paginator(animales_list, 5)  # o el número que desees por página
    page = request.GET.get('page')
    animales = paginator.get_page(page)
    return render(request, 'wiki/animales.html', {'animales': animales})

def armas(request):
    armas_list = Arma.objects.all().order_by('numero')  # Ahora ordena por número
    paginator = Paginator(armas_list, 5)  # 5 armas por página
    page = request.GET.get('page')
    
    try:
        armas = paginator.page(page)
    except PageNotAnInteger:
        armas = paginator.page(1)
    except EmptyPage:
        armas = paginator.page(paginator.num_pages)
        
    return render(request, 'wiki/Armas.html', {'armas': armas})

@login_required(login_url='inicio_sesion_admin')
def panel_administrador(request):
    if not (request.user.is_superuser or getattr(request.user, 'rol', None) and request.user.rol.nombre == 'Administrador'):
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    
    usuarios_list = Usuario.objects.all().order_by('email')
    paginator = Paginator(usuarios_list, 10)  # 10 usuarios por página
    page = request.GET.get('page')
    
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        usuarios = paginator.page(1)
    except EmptyPage:
        usuarios = paginator.page(paginator.num_pages)
        
    return render(request, 'wiki/panel_administrador.html', {'usuarios': usuarios})

# Las demás vistas permanecen igual (sin paginación)
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

@login_required(login_url='inicio_sesion_wiki')
def micuentatf(request):
    usuario = request.user
    if request.method == 'POST':
        if 'guardar' in request.POST:
            nuevo_email = request.POST.get('email')
            nueva_password = request.POST.get('password')
            nueva_imagen = request.FILES.get('imagen')

            if not nuevo_email:
                messages.error(request, 'El correo es obligatorio.')
                return redirect('micuentatf')

            if Usuario.objects.exclude(pk=usuario.pk).filter(email=nuevo_email).exists():
                messages.error(request, 'El correo ya está registrado.')
                return redirect('micuentatf')

            usuario.email = nuevo_email
            if nueva_password:
                usuario.password = make_password(nueva_password)
            if nueva_imagen:
                usuario.imagen = nueva_imagen

            usuario.save()
            messages.success(request, 'Datos actualizados correctamente.')
            return redirect('micuentatf')

        elif 'eliminar' in request.POST:
            usuario.delete()
            logout(request)
            messages.success(request, 'Cuenta eliminada.')
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
            usuario.password = make_password(nueva_password)
            update_session_auth_hash(request, usuario)

        usuario.save()
        messages.success(request, 'Información actualizada.')
        return redirect('micuentatf')

    return render(request, 'wiki/editar_informacion.html', {'usuario': usuario})

@login_required(login_url='inicio_sesion_wiki')
def editar_usuario(request, id):
    if not request.user.is_superuser and request.user.rol.nombre != 'Administrador':
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
def eliminar_usuario(request, id):
    if not request.user.is_superuser and request.user.rol.nombre != 'Administrador':
        return HttpResponseForbidden("No tienes permiso para eliminar usuarios.")

    usuario = get_object_or_404(Usuario, id=id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, "Usuario eliminado correctamente.")
        return redirect('panel_administrador')

    return render(request, 'wiki/confirmar_eliminar.html', {'usuario': usuario})

def inicio_sesion_wiki(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(password, usuario.password):
                login(request, usuario)
                return redirect('menuprincipal_wiki')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo no registrado.')
    return render(request, 'wiki/inicio_sesion_wiki.html')

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
        hashed_password = make_password(password1)
        nuevo_usuario = Usuario(email=email, password=hashed_password, rol=rol_default)
        nuevo_usuario.save()
        messages.success(request, '¡Usuario registrado con éxito! Ahora puedes iniciar sesión.')
        return redirect('inicio_sesion_wiki')

    return render(request, 'wiki/registrase_wiki.html')

def inicio_sesion_admin(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        password = request.POST.get('password')
        try:
            usuario = Usuario.objects.get(email=email)
            if check_password(password, usuario.password):
                if usuario.rol.nombre == 'Administrador' or usuario.is_superuser:
                    login(request, usuario)
                    return redirect('panel_administrador')
                else:
                    messages.error(request, 'No tienes permisos de administrador.')
            else:
                messages.error(request, 'Contraseña incorrecta.')
        except Usuario.DoesNotExist:
            messages.error(request, 'Correo no registrado.')
    return render(request, 'wiki/inicio_sesion_admin.html')

@login_required(login_url='inicio_sesion_wiki')
def panel_administrador_redirect(request):
    if request.user.is_superuser or (hasattr(request.user, 'rol') and request.user.rol.nombre == 'Administrador'):
        return redirect('panel_administrador')
    else:
        messages.error(request, "No tienes permisos para acceder al panel de administrador.")
        return redirect('menuprincipal_wiki')

@login_required
def editar_animales(request):
    animales_list = Animal.objects.all().order_by('numero') 
    paginator = Paginator(animales_list, 5)  # 5 animales por página
    page = request.GET.get('page')
    
    try:
        animales = paginator.page(page)
    except PageNotAnInteger:
        animales = paginator.page(1)
    except EmptyPage:
        animales = paginator.page(paginator.num_pages)
        
    return render(request, 'wiki/editar_animales.html', {'animales': animales})

@login_required
def editar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.nombre = request.POST.get('nombre')
        animal.hostilidad = request.POST.get('hostilidad')
        animal.descripcion = request.POST.get('descripcion')

        if 'imagen' in request.FILES:
            animal.imagen = request.FILES['imagen']

        animal.save()
        messages.success(request, 'Animal actualizado correctamente.')
        return redirect('editar_animales')

    return render(request, 'wiki/editar_animal.html', {'animal': animal})

@login_required
def eliminar_animal(request, id):
    animal = get_object_or_404(Animal, id=id)
    if request.method == 'POST':
        animal.delete()
        messages.success(request, 'Animal eliminado correctamente.')
        return redirect('editar_animales')

    return render(request, 'wiki/eliminar_animal.html', {'animal': animal})

@login_required
def editar_armas(request):
    armas_list = Arma.objects.all().order_by('numero') 
    paginator = Paginator(armas_list, 5)  # 5 armas por página
    page = request.GET.get('page')
    
    try:
        armas = paginator.page(page)
    except PageNotAnInteger:
        armas = paginator.page(1)
    except EmptyPage:
        armas = paginator.page(paginator.num_pages)
        
    return render(request, 'wiki/editar_armas.html', {'armas': armas})

@login_required
def editar_arma(request, id):
    arma = get_object_or_404(Arma, id=id)
    if request.method == 'POST':
        arma.nombre = request.POST.get('nombre')
        arma.tipo = request.POST.get('tipo')
        arma.descripcion = request.POST.get('descripcion')
        if request.FILES.get('imagen'):
            arma.imagen = request.FILES.get('imagen')
        arma.save()
        messages.success(request, "Arma actualizada correctamente.")
        return redirect('editar_armas')
    return render(request, 'wiki/editar_arma.html', {'arma': arma})

@login_required
def eliminar_arma(request, id):
    arma = get_object_or_404(Arma, id=id)
    if request.method == 'POST':
        arma.delete()
        messages.success(request, "Arma eliminada correctamente.")
        return redirect('editar_armas')
    return render(request, 'wiki/eliminar_arma.html', {'arma': arma})