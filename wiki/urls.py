from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.menuprincipal_wiki, name='menuprincipal_wiki'),
    path('menuprincipal_wiki/', views.menuprincipal_wiki, name='menuprincipal_wiki'),
    path('animales/', views.animales, name='animales'),
    path('construcciones/', views.construcciones, name='construcciones'),
    path('consumibles/', views.consumibles, name='consumibles'),
    path('enemigos/', views.enemigos, name='enemigos'),
    path('flora/', views.flora, name='flora'),
    path('forowiki/', views.forowiki, name='forowiki'),
    path('historia/', views.historia, name='historia'),
    path('inicio_sesion_wiki/', views.inicio_sesion_wiki, name='inicio_sesion_wiki'),
    path('logros/', views.logros, name='logros'),
    path('lugarestf/', views.lugarestf, name='lugarestf'),
    path('micuentatf/', views.micuentatf, name='micuentatf'),
    path('recuperarcontra/', views.recuperarcontra, name='recuperarcontra'),
    path('registrase_wiki/', views.registrase_wiki, name='registrase_wiki'),
    path('micuentatf/editar/', views.editar_informacion, name='editar_informacion'),
    path('editar/', views.editar_informacion, name='editar_informacion'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('panel_administrador/editar/<int:id>/', views.editar_usuario, name='editar_usuario'),
    path('panel_administrador/eliminar/<int:id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('admin_login/', views.inicio_sesion_admin, name='inicio_sesion_admin'),
    path('panel_administrador/', views.panel_administrador, name='panel_administrador'),
    path('ir_a_panel_administrador/', views.panel_administrador_redirect, name='panel_administrador_redirect'),

    # Animal
    path('editar_animales/', views.editar_animales, name='editar_animales'),
    path('editar_animal/<int:id>/', views.editar_animal, name='editar_animal'),
    path('eliminar_animal/<int:id>/', views.eliminar_animal, name='eliminar_animal'),

    # armas
    path('armas/', views.armas, name='armas'),
    path('editar_armas/', views.editar_armas, name='editar_armas'),
    path('editar_arma/<int:id>/', views.editar_arma, name='editar_arma'),
    path('eliminar_arma/<int:id>/', views.eliminar_arma, name='eliminar_arma'),
    path('editar_armas/', views.editar_armas, name='editar_armas'),

    path('enemigos/editar/', views.lista_enemigos, name='editar_enemigos'),
    path('enemigos/editar/<int:enemigo_id>/', views.editar_enemigo, name='editar_enemigo'),
    path('enemigos/eliminar/<int:enemigo_id>/', views.eliminar_enemigo, name='eliminar_enemigo'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
