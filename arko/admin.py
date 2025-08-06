from django.contrib import admin
from .models import Regiao, Estado, Mesoregiao, Microregiao, RegiaoIntermediaria, RegiaoImediata, Municipio, Distrito
# Register your models here.



@admin.register(Regiao)
class RegiaoAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'sigla', 'nome')
    search_fields = ('nome', 'sigla', 'id_ibge')

@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'sigla', 'nome', 'regiao')
    search_fields = ('nome', 'sigla', 'id_ibge')
    list_filter = ('regiao',)

@admin.register(Mesoregiao)
class MesoregiaoAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'estado')
    search_fields = ('nome', 'id_ibge')
    list_filter = ('estado',)

@admin.register(Microregiao)
class MicroregiaoAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'mesoregiao')
    search_fields = ('nome', 'id_ibge')
    list_filter = ('mesoregiao',)

@admin.register(RegiaoIntermediaria)
class RegiaoIntermediariaAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'estado')
    search_fields = ('nome', 'id_ibge')
    list_filter = ('estado',)

@admin.register(RegiaoImediata)
class RegiaoImediataAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'regiao_intermediaria')
    search_fields = ('nome', 'id_ibge')
    list_filter = ('regiao_intermediaria',)

@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'microrregiao', 'mesoregiao', 'estado', 'regiao_imediata', 'regiao_intermediaria')
    search_fields = ('nome', 'id_ibge')
    list_filter = ('estado', 'mesoregiao', 'microrregiao', 'regiao_imediata', 'regiao_intermediaria')

@admin.register(Distrito)
class DistritoAdmin(admin.ModelAdmin):
    list_display = ('id_ibge', 'nome', 'municipio')
    search_fields = ('nome', 'id_ibge')
    autocomplete_fields = ['municipio']

