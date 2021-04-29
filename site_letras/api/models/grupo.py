from django.db import models

from .artista import Artista


class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    sobre = models.TextField()
    data_fundacao = models.DateField(blank=True, null=True)
    tipos = (
        ("grupo", "Grupo"),
        ("banda", "Banda"),
    )
    integrantes = models.ManyToManyField(Artista)

    def __str__(self):
        return self.nome