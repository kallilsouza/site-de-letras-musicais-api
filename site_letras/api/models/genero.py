from django.db import models


class Genero(models.Model):
    nome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "gênero"
        verbose_name_plural = "gêneros"

    def __str__(self):
        return self.nome