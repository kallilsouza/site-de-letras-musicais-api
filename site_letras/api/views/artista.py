from rest_framework import status, viewsets
from ..mixins.read_write_serializer_mixin import ReadWriteSerializerMixin
import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from ..serializers.artista import ArtistaReadSerializer, ArtistaWriteSerializer

from ..models import Artista


class ArtistaViewSet(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    queryset = Artista.objects.all()

    read_serializer_class = ArtistaReadSerializer
    write_serializer_class = ArtistaWriteSerializer