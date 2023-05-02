from django.urls import path, include
from .views import index, lista_projetos_view, popular_banco, detalhes_projeto
from rest_framework import routers
from listaprojetos.views import ProjetosViewSet


router = routers.DefaultRouter()

router.register(r"dataprojetos", ProjetosViewSet)


urlpatterns = [
    path("", index, name="index"),
    path("api/", include(router.urls)),
    path("lista-projetos/", lista_projetos_view, name="lista_projetos"),
    path("data/", popular_banco, name="popular_banco"),
    path('lista-projetos/<int:projeto_id>/', detalhes_projeto, name='detalhes_projeto'),

]
