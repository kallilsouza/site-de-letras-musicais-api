from django.db import models


from .artista import Artista
from .grupo import Grupo


class Cancao(models.Model):
    nome = models.CharField(max_length=100)
    artista_principal = models.ForeignKey(
        Artista, on_delete=models.CASCADE, blank=True, null=True
    )
    artistas = models.ManyToManyField(Artista, related_name="artistas")
    grupo = models.ForeignKey(Grupo, on_delete=models.SET_NULL, blank=True, null=True)
    data_lancamento = models.DateField(blank=True, null=True)

    letra = models.TextField()

    class Meta:
        verbose_name = "canção"
        verbose_name_plural = "canções"

    def __str__(self):
        artistas = self.artista_principal.nome
        if self.artistas:
            ar = []
            for a in self.artistas.all():
                ar.append(a.nome)
            artistas = ", ".join(ar)

        return "{nome} - {artistas}".format(nome=self.nome, artistas=artistas)
