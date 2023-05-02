from django.urls import path, include
from .views import lista_projetos_view, detalhes_projeto
from rest_framework import routers
from listaprojetos.views import ProjetosViewSet


router = routers.DefaultRouter()

router.register(r"dataprojetos", ProjetosViewSet)


urlpatterns = [
    path("",  lista_projetos_view, name="lista_projetos"),
    path("api/", include(router.urls)),
    path(r'<int:projeto_id>/', detalhes_projeto, name='detalhes_projeto'),

]
