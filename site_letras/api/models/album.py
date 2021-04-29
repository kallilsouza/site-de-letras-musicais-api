from django.db import models

from .artista import Artista
from .genero import Genero
from .grupo import Grupo


class Album(models.Model):
    nome = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, null=True, blank=True)
    data_lancamento = models.DateField(blank=True, null=True)
    genero = models.ForeignKey(Genero, blank=True, null=True, on_delete=models.SET_NULL)
    tipos = (
        ("album", "Álbum"),
        ("single", "Single"),
    )
    tipo = models.CharField(choices=tipos, max_length=20)

    def __str__(self):
        dono = self.artista
        if self.grupo:
            dono = self.grupo

        ano = ""
        if self.data_lancamento:
            ano = "({ano})".format(ano=self.data_lancamento.year)

        return "{nome} - {dono} {ano}".format(nome=self.nome, dono=dono, ano=ano)

    class Meta:
        verbose_name = "álbum"
        verbose_name_plural = "álbuns"
