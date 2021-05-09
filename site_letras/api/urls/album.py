from django.urls import path, include
from ..views.album import AlbumViewSet
from rest_framework.routers import DefaultRouter

album_router = DefaultRouter()
album_router.register("albuns", AlbumViewSet, basename="albuns")
