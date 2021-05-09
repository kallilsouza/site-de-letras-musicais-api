from django.urls import path, include, re_path

from .artista import artista_router
from .cancao import cancao_router
from .album import album_router

urlpatterns = [
    path("", include(artista_router.urls)),
    path("", include(cancao_router.urls)),
    path("", include(album_router.urls)),
]
