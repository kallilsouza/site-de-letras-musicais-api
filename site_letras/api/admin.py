from django.contrib import admin

from .models import *


class FaixasInline(admin.TabularInline):
    model = Faixa
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    fields = ("nome", "artista", "data_lancamento", "genero", "tipo")

    inlines = [FaixasInline]


admin.site.register(Artista)
admin.site.register(Cancao)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Faixa)
admin.site.register(Genero)
admin.site.register(Pais)

# Register your models here.
