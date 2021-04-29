from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models.artista import Artista


class ArtistaReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ("id", "nome", "sobre", "pais", "data_nascimento")


class ArtistaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ("nome", "sobre", "pais", "data_nascimento")
