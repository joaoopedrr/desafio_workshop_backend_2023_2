# Projeto de cadastro do workshop da fábrica de software_Back-

1-Entrar no VScode

1- Criar uma pasta vazia

2- Abrir o terminal
no teclado = CTRL + J

3- Instalar o ambiente virtual
COMANDO = python -m venv venv

3- Ativar o ambiente virtual:

se for linux/MAC:
    .\venv\bin\activate.ps1

se for Windows:
    .\venv\Scripts\activate.ps1

4- Baixar o djangorestframework
COMANDO = pip install djangorestframework

5- Baixar o projeto na pasta
COMANDO = django-admin startproject nomedapasta .

6- Criar o app 
COMANDO = python .\manage.py startapp nomedoapp

7- Dar um ls pra ver onde a pasta ta alocada no diretorio
COMANDO = ls

8- A.Vai na settings
    B.Coloca dentro da "installedapps" (nome rest_framework e o nome do app)
    C.Não esquecer a virgula

9- A. "fazer o "python manage.py makemigrations"
   B. "fazer o python manage.py migrate"
    C. "fazer o python manage.py runserver"

10- Criar dois arquivos no app, o serializers.py e o urls.py

11- Importar na models from django.db import models

12- Modificar a models para adicionar as classes e a tabela pra recolher os dados.

13- No serializers, digite em cima "from rest_framework import serializers" e "from .models import models"

14- Criamos as classes serializer para converter de python para json e vice versa (serializers.ModelSerializer): -dentro de uma classe serializer criar a classe Meta: -Colocar o modelo -Selecionar os fields

15- A. Criar as views e jogar o serializers dentro: -"from rest_framework import viewsets"- -"from .models import modelo" -"from .serializers import classeSerializer" -

    B. Adicionar as classes para puxar os objetos do modelo e transportar o serializer para viewset.

16- Ir para urls do app -from rest_framework import routers -from .views import classeviewset -Setar o router como DefaultRouter() -registra os routers das viewsets -urlpatterns = router.urls.

17- Ir para urls do projeto -importar o include -criar o path da urls criada no app.

18- Python manage.py makemigrations -python manage.py migrate -python manage.py runserver.

19- Ir no navegador pra ver se houve mudança, ver se aparece o "/nomedeterminadonaurl"

20- Fazer o download e instalar o postgresql(meu caso).
    -OBS: Pode ser feito por outro banco de dados.

21- A. Ir em "servers" no programa, na parte superior da esquerda da tela inicial.
    B. Ir em "create" e rodar

22- Voltar pro Vscode:
            -Digitar os comandos:
                                1.
                                'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'clinicavet',
             'USER': 'postgres',
             'PASSWORD': 'mypassword',
             'HOST': 'localhost',
             'PORT': '5433',
        'OPTIONS': {
            'options': '-c search_path=public'
        },}
        'ATOMIC_REQUESTS': True, 
                                2.
                                pip install psycopg2
                                3.
                                pip install psycopg-binary
                                4.
                                pip install postgres
                                5.
                                pip install sqlparse

23- Testar no servidor novamente

24- Criar o "requirements.txt" em um arquivo normal no projeto

25- Criar o ".gitignore" em um arquivo normal no projeto 

26- Colocar dentro do arquivo o comando "/venv" para retirar os arquivos desnecessários para quando for subir no github.

27. Ir no terminal e digitar os comandos:
    1.git init
    2.git add .
    3.git commit -m "sua legenda"
    4.git branch -M main
    5.git remote add origin "link do seu repositório"
    6.git push -u origin main

28- Ir no seu repositório, atualizar e ver se estar tudo correto.

29- FIM
