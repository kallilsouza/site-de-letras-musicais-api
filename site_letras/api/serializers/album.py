from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models.album import Album


class AlbumReadSerializer(serializers.ModelSerializer):
    artista = serializers.SerializerMethodField()
    genero = serializers.SerializerMethodField()
    faixas = serializers.SerializerMethodField()

    def get_artista(self, obj):
        artista = obj.artista
        data = {"nome": artista.nome, "id": artista.id}
        return data

    def get_genero(self, obj):
        genero = obj.genero
        data = {"nome": genero.nome, "id": genero.id}
        return data

    def get_faixas(self, obj):
        faixas = obj.faixa_set.all().order_by("numero")
        data = {}
        for faixa in faixas:
            data[faixa.numero] = {
                "nome": faixa.cancao.nome,
                "id": faixa.id,
            }
        return data

    class Meta:
        model = Album
        fields = (
            "id",
            "nome",
            "artista",
            "genero",
            "data_lancamento",
            "tipo",
            "faixas",
        )


class AlbumWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "nome", "artista", "genero", "data_lancamento", "tipo")