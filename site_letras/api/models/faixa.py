from django.db import models

from .album import Album
from .cancao import Cancao


class Faixa(models.Model):
    numero = models.IntegerField()
    cancao = models.ForeignKey(Cancao, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return "{numero} - {cancao} - {album}".format(
            numero=str(self.numero), cancao=self.cancao.nome, album=self.album.nome
        )
