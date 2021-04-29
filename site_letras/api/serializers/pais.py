from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models.pais import Pais


class PaisReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ("id", "nome")


class PaisWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = "nome"
