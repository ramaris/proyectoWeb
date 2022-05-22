from xml.dom.minidom import Document
from django.urls import path

from ProyectoWebapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.home, name="home"),
    path('tienda',views.tienda, name="Tienda"),
    path('blog',views.blog, name="Blog"),
    path('contacto',views.contacto, name="Contacto"),
]

urlpatterns+=static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)