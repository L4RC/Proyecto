from django.urls import path

from . import views
#from django.conf import settings
#from django.conf.urls.static import static 

urlpatterns = [
    path('', views.Iniciar, name="Iniciar"),    
    path('', views.Student, name="Student"),
    path('', views.Registro, name="Registro"),

]