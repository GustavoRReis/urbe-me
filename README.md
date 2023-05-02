# Projeto Urbe.me

A aplicação desenvolvida em Python com o framework Django, tem como objetivo facilitar a renderização de projetos, onde é possivel acessar sua localização e detalhes, facilitando ao usuário uma pesquisa para futuro investimento.

# Configuração mínima

Na sua máquina você deve ter:

 - Python 3.10.6

# Tecnologias Utilizadas

- Linguagem de Programação: Python
- Django
- DjangoRestFramework



# Funcionalidades da API
- Realizar um Get para listar todos os projetos.

# Instalação
## Passo 1:
- Clone este repositório em sua máquina local.
## Passo 2:
- Com o projeto em sua máquina local, crie um ambiente virtual para gerenciar as dependências do projeto.
- `python3 -m venv venv`
- Acesse com o comando:
- `source venv/bin/activate`
## Passo 3:
- Instale dentro do ambiente virtual as seguintes dependências.
- `pip install Django djangorestframework folium python-dotenv` 
- Após a instalação você deve criar um arquivo .env na raiz do projeto com os seguintes dados dentro do arquivo:
- SECRET_KEY = django-insecure-_$1f_8fs!4u^nvq+2+y2czy%mq7py+7it1_@hvy4vp0njzf9t&`
- É de suma importância que o arquivo .env tenha exatamente esse conteudo.
## Passo 4:
- Dentro do ambiente virtual execute o seguinte comando para popular o banco de dados.
- `python3 manage.py migrate`
- Após popular, basta executar o comando para subir o projeto:
- `python manage.py runserver`

## Execução
- Basta abrir o projeto na rota padrao http://127.0.0.1:8000/ ou a rota fornecida ao executar o runserver



## Considerações Finais
- Este é um projeto de exemplo, não recomendado para uso em produção sem uma revisão criteriosa e ajustes nas configurações de segurança.

- O projeto foi realizado com o objetivo de criar uma simples aplicação django com duas rotas. No desafio foi dado como sugestão a utilização de uma API.
- Ao analizar e projetar o desenvolvimento, escolhi por consumir a API. Durante o desenvolvimento, precisamente no momento de criar a rota para cada card, tive que mudar minha estratégia, decidi criar meu proprio banco, populando apenas com os 9 primeiros dicionarios vindos da API. A partir desse momento segui com meu plano para concluir o desenvolvimento. O histórico de commits registra um pouco da minha tomada de decisões.
