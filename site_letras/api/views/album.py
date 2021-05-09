from rest_framework import status, viewsets
from ..mixins.read_write_serializer_mixin import ReadWriteSerializerMixin
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from functools import reduce
import operator


from ..serializers.album import AlbumReadSerializer, AlbumWriteSerializer

from ..models import Album


def nome(queryset, filtro, nome):
    # Obs.: a variável 'nome' pode conter mais de um nome (ex.: Silvio Santos)
    lista_termos = nome.split(
        " "
    )  # separa cada nome e guarda cada um deles em uma lista
    queryset = queryset.filter(
        Q(
            # verifica se o primeiro nome contém cada nome em 'lista_termos'
            # (ignorando se as letras são minúsculas ou maiúsculas)
            reduce(operator.or_, (Q(nome__icontains=x) for x in lista_termos))
        )
    )
    return queryset


def nome_exato(queryset, filtro, nome):
    return queryset.filter(nome=nome)


def nome_artista(queryset, filtro, nome):
    # Obs.: a variável 'nome' pode conter mais de um nome (ex.: Silvio Santos)
    lista_termos = nome.split(
        " "
    )  # separa cada nome e guarda cada um deles em uma lista
    queryset = queryset.filter(
        Q(
            # verifica se o primeiro nome contém cada nome em 'lista_termos'
            # (ignorando se as letras são minúsculas ou maiúsculas)
            reduce(operator.or_, (Q(artista__nome__icontains=x) for x in lista_termos))
        )
    )
    return queryset


def ordem_alfabetica(queryset, filter, ordem):
    if ordem == True:
        return queryset.order_by("nome")
    return queryset


class AlbumFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(method=nome)
    nome_exato = django_filters.CharFilter(method=nome_exato, label="Nome exato")
    nome_artista = django_filters.CharFilter(
        method=nome_artista, label="Nome do artista"
    )
    ordem_alfabetica = django_filters.BooleanFilter(
        method=ordem_alfabetica, label="Ordem alfabética"
    )

    class Meta:
        model = Album
        fields = ["nome"]


class AlbumViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    queryset = Album.objects.all()

    read_serializer_class = AlbumReadSerializer
    write_serializer_class = AlbumWriteSerializer

    filter_backends = [DjangoFilterBackend]
    filter_class = AlbumFilter

    http_method_names = ["get"]