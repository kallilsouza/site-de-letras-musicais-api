from django.urls import path, include, re_path

from .artista import artista_router
from .cancao import cancao_router

urlpatterns = [
    path("", include(artista_router.urls)),
    path("", include(cancao_router.urls)),
]
