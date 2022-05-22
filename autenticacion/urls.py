from xml.dom.minidom import Document
from django.urls import path

from .views import VRregistro, cerrar_sesion, loguear
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    

    path('',VRregistro.as_view(), name="autentincacion"),
    path('cerrar sesion',cerrar_sesion, name="cerrar_sesion"),
    path('loguear',loguear, name="loguear"),

]


