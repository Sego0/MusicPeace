from django.urls import path
from Peace import views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.ini, name="Inicio"),
    path("Sobre/",views.sob, name="Sobre"),
    path("Creacion/",views.crea, name="Creacion"),
    path("Usuarios/",views.usu, name="Usuarios"),
    path("Login/",LoginView.as_view(template_name= "log.html") , name="login"),
    path("Logout/",LogoutView.as_view() , name="Logout"),
    path("Register/",views.reg , name="register"),
    path("delete/<int:post_id>/", views.delete, name="delete"),
    path("profile/<str:username>/", views.profile, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
