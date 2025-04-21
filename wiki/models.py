from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class RolUsuario(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        rol_id = extra_fields.pop('rol', None)
        if rol_id is not None and isinstance(rol_id, int):
         extra_fields['rol'] = RolUsuario.objects.get(pk=rol_id)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('rol') is None:
            rol_admin, created = RolUsuario.objects.get_or_create(nombre='Administrador')
            extra_fields['rol'] = rol_admin

        return self.create_user(email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    rol = models.ForeignKey('RolUsuario', on_delete=models.SET_NULL, null=True)
    imagen = models.ImageField(upload_to='usuarios/', null=True, blank=True)  # NUEVO
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    
    
class Animal(models.Model):
    numero = models.IntegerField()
    nombre = models.CharField(max_length=100)
    hostilidad = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='animales/', null=True, blank=True)

    def __str__(self):
        return f"{self.numero}. {self.nombre}"
    
class Arma(models.Model):
    numero = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to='armas/')
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre