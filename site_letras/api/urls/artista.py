from django.urls import path, include
from ..views.artista import ArtistaViewSet
from rest_framework.routers import DefaultRouter

artista_router = DefaultRouter()
artista_router.register("artistas", ArtistaViewSet, basename="artistas")
