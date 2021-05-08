from django.urls import path, include
from ..views.cancao import CancaoViewSet
from rest_framework.routers import DefaultRouter

cancao_router = DefaultRouter()
cancao_router.register("cancoes", CancaoViewSet, basename="cancoes")
