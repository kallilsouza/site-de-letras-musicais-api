from django.db import models

from .pais import Pais


class Artista(models.Model):
    nome = models.CharField(max_length=100)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, blank=True, null=True)
    sobre = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    imagem = models.ImageField(upload_to="imagens/artistas/", blank=True, null=True)

    def __str__(self):
        return self.nome