from django.shortcuts import render
import requests


def index(request):
    return render(request, 'listaprojetos/homepage.html')


def lista_projetos_view(request):
    url = 'https://urbe.me/administracao/api/lista-projetos/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except Exception as error:
        print("Erro na chamada da API:", error)
    context = {'projetos': data}
    return render(request, 'listaprojetos/homepage.html', context)
