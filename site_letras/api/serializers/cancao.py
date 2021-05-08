from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from ..models.cancao import Cancao


class CancaoReadSerializer(serializers.ModelSerializer):
    artista_principal = serializers.SerializerMethodField()
    artistas = serializers.SerializerMethodField()
    albums = serializers.SerializerMethodField()

    def get_artista_principal(self, obj):
        artista = obj.artista_principal
        data = {"nome": artista.nome, "id": artista.id}
        return data

    def get_artistas(self, obj):
        artistas = []
        for artista in obj.artistas.all():
            data = {"nome": artista.nome, "id": artista.id}
            artistas.append(data)
        return artistas

    def get_albums(self, obj):
        albums = []
        for faixa in obj.faixa_set.all():
            album = faixa.album
            data = {
                "nome": album.nome,
                "artista": {"nome": album.artista.nome, "id": album.artista.id},
                "data_lancamento": album.data_lancamento,
                "id": album.id,
            }
            albums.append(data)

        return albums

    class Meta:
        model = Cancao
        fields = (
            "id",
            "nome",
            "artista_principal",
            "artistas",
            "data_lancamento",
            "letra",
            "albums",
        )


class CancaoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cancao
        fields = (
            "nome",
            "artista_principal",
            "artistas",
            "data_lancamento",
            "letra",
        )
