
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Utilizador/',include('Utilizador.urls')),
    path('api/Membros/',include('Membros.urls')),
]