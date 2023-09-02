from rest_framework import viewsets
from films.api import serializers
from films import models

class FilmsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.FilmsSerializer
    queryset = models.Films.objects.all()

class ElencoViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ElencoSerializer
    queryset = models.Elenco.objects.all()