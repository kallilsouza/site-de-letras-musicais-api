from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models.artista import Artista
from .pais import PaisReadSerializer


class ArtistaReadSerializer(serializers.ModelSerializer):
    pais = PaisReadSerializer()

    class Meta:
        model = Artista
        fields = ("id", "nome", "sobre", "pais", "data_nascimento")


class ArtistaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artista
        fields = ("nome", "sobre", "pais", "data_nascimento")
