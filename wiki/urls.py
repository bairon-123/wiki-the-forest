from django.urls import path 
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.menuprincipal_wiki, name='menuprincipal_wiki'),  
    path('animales/', views.animales, name='animales'),
    path('armas/', views.armas, name='armas'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('flora/', views.flora, name='flora'),
    path('forowiki/', views.forowiki, name='forowiki'),
    path('historia/', views.historia, name='historia'),
    path('inicio_sesion_wiki/', views.inicio_sesion_wiki, name='inicio_sesion_wiki'),
    path('logros/', views.logros, name='logros'),
    path('lugarestf/', views.lugarestf, name='lugarestf'),
    path('menuprincipal_wiki/', views.menuprincipal_wiki, name='menuprincipal_wiki'),
    path('micuentatf/', views.micuentatf, name='micuentatf'),
    path('recuperarcontra/', views.recuperarcontra, name='recuperarcontra'),
    path('registrase_wiki/', views.registrase_wiki, name='registrase_wiki'),
    path('micuentatf/editar/', views.editar_informacion, name='editar_informacion'),
    path('editar/', views.editar_informacion, name='editar_informacion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('panel_administrador/', views.panel_administrador, name='panel_administrador'),
    path('panel_administrador/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('panel_administrador/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('redirigir_panel_admin/', views.panel_administrador_redirect, name='redirigir_panel_admin'),
]