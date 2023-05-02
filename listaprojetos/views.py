from django.shortcuts import render
import requests
from .models import Projetos
from django.http import HttpResponse
from rest_framework import viewsets
from listaprojetos.serializer import ProjetosSerializer


def index(request):
    return render(request, "listaprojetos/homepage.html")


def popular_banco(request):

    if request.session.get('db_populado'):
        return HttpResponse("O banco de dados já foi populado!")

    url = "https://urbe.me/administracao/api/lista-projetos/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as error:
        print("Erro na chamada da API:", error)
        data = []

    for item in data[:9]:
        projeto = Projetos(
            projeto=item.get("projeto"),
            latitude=item.get("latitude"),
            longitude=item.get("longitude"),
            tir_media=item.get("tir_media"),
            total_captado=item.get("total_captado"),
            vgv=item.get("vgv"),
        )
        projeto.save()

    request.session['db_populado'] = True

    return HttpResponse("Banco de dados populado com sucesso!")


def lista_projetos_view(request):
    projetos = Projetos.objects.all()
    context = {"projetos": projetos}
    return render(request, "listaprojetos/homepage.html", context)


def detalhes_projeto(request, projeto_id):
    try:
        projeto = Projetos.objects.get(id=projeto_id)
    except Exception as error:
        print("Erro na chamada da API:", error)
        projeto = None
    context = {"projeto": projeto}
    return render(request, "listaprojetos/detalhes_projeto.html", context)


class ProjetosViewSet(viewsets.ModelViewSet):
    queryset = Projetos.objects.all()
    serializer_class = ProjetosSerializer
