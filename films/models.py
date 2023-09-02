from django.db import models
from uuid import uuid4

def upload_image_film(instance, filename):
    return f"{instance.id_film}-{filename}"

# MINHA PRIMEIRA CLASSE
class Elenco(models.Model):
    ator_principal = models.CharField(max_length=255)
    ator_secundário = models.CharField(max_length=255)
    ator_terciário = models.CharField(max_length=255)

    # FUNÇÃO IDENTADA
    def __str__(self):
        return f'Atores: {self.ator_principal}, {self.ator_secundário}, {self.ator_terciário}'


# MINHA SEGUNDA CLASSE
class Films(models.Model):
    id_film = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    valor = models.FloatField(max_length=50, help_text='Preço do filme', blank=True,verbose_name= "VALOR: ")
    titulo = models.CharField(max_length=255, help_text='Nome do filme', blank=True,verbose_name= "TÍTULO: ")
    diretor = models.CharField(max_length=255, help_text='Nome e Sobrenome', blank=True,verbose_name= "DIRETOR: ")
    ano_de_lançamento = models.IntegerField(help_text='Lançamento da obra', blank=True,verbose_name= "ANO DE LANÇAMENTO: ")
    avaliação = models.CharField(max_length=255, help_text='Opinião', blank=True,verbose_name= "AVALIAÇÃO: ")
    duração = models.FloatField(max_length=255, help_text='Duração em minutos', blank=True,verbose_name= "DURAÇÃO: ")
    produtora = models.CharField(max_length=255, help_text='Empresa', blank=True,verbose_name= "PRODUTORA: ")
    create_add = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to=upload_image_film, blank=True, null=True)
    elenco = models.ForeignKey(Elenco, on_delete=models.CASCADE)

    # FUNÇÃO IDENTADA
    def __str__(self):
        return f'Título do Filme: {self.titulo}'

