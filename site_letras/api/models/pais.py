from django.db import models


class Pais(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        verbose_name = "país"
        verbose_name_plural = "países"

    def __str__(self):
        return self.nome