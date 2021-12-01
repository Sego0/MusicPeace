from django.urls import path
from Peace import views

urlpatterns = [
    path("",views.ini, name="Inicio"),
    path("Sobre/",views.sob, name="Sobre"),
    path("Creacion/",views.crea, name="Creacion"),
    path("Usuarios/",views.usu, name="Usuarios"),
]
