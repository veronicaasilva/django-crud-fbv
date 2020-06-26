from django.urls import path
from .views import deslogar_usuario, logar_usuario, novo_usuario

urlpatterns = [
    path('login/', logar_usuario, name='login'),
    path('logout/', deslogar_usuario, name='logout'),
    path('novousuario/', novo_usuario, name='novo_usuario')
   
]
