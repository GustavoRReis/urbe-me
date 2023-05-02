from django.urls import path
from listaprojetos.views import index, lista_projetos_view

urlpatterns = [
    path("", index),
    path("lista-projetos/", lista_projetos_view),
]
