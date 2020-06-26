
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('djangoadmin/', admin.site.urls),
    path('', include('clientes.urls')),
    path('auth/', include ('autenticacao.urls')),
]
