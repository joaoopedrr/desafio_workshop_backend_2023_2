from rest_framework import serializers
from films import models

# MINHA PRIMEIRA CLASSE
class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Films
        fields = '__all__'

# MINHA SEGUNDA CLASSE
class ElencoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Elenco
        fields = '__all__'
        
