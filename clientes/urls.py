from django.urls import path
from .views import listar_clientes, clonar_cliente, cadastrar_cliente, atualizar_cliente

urlpatterns = [
   path('', listar_clientes, name='listar_clientes'),
   path('clonar_cliente/<int:id>', clonar_cliente, name='clonar_cliente'),
   path('cadastrar_cliente', cadastrar_cliente, name='cadastrar_cliente'),
   path('atualizar_cliente/<int:id>', atualizar_cliente, name='atualizar_cliente'),
]