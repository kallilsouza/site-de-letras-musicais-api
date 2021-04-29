from django.urls import path, include, re_path

from .artista import artista_router

urlpatterns = [
    path("", include(artista_router.urls)),
]
