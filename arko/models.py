from django.db import models

# Create your models here.
'''utilizando f-strings para nomear as tabelas e relacionamentos, 
utilizo dbeaver como sgdb e considero uma boa pratica 
nomear a tabela como app_nome_do_model'''

class Regiao(models.Model):
    id_ibge = models.IntegerField()
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    class Meta:
        app_label = 'arko'
        verbose_name = "Região"
        verbose_name_plural = "Regiões"
        db_table = f'{app_label}_Regiao'
    def __str__(self):
        return self.nome


class Estado(models.Model):
    id_ibge = models.IntegerField()
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    regiao = models.ForeignKey(Regiao, on_delete=models.CASCADE, related_name="estados")
    class Meta:
        app_label = 'arko'
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        db_table = f'{app_label}_Estado'
    def __str__(self):
        return self.nome


class Mesoregiao(models.Model):
    id_ibge = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="mesoregioes")
    class Meta:
        app_label = 'arko'
        verbose_name = "Mesorregião"
        verbose_name_plural = "Mesorregiões"
        db_table = f'{app_label}_Mesoregiao'
    def __str__(self):
        return self.nome


class Microregiao(models.Model):
    id_ibge = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    mesoregiao = models.ForeignKey(Mesoregiao, on_delete=models.CASCADE, related_name="microregioes", null=True, blank=True)
    class Meta:
        app_label = 'arko'
        verbose_name = "Microrregião"
        verbose_name_plural = "Microrregiões"
        db_table = f'{app_label}_Microregiao'
    def __str__(self):
        return self.nome
    

class RegiaoIntermediaria(models.Model):
    id_ibge = models.IntegerField()
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="regioes_intermediarias", null=True, blank=True)
    class Meta:
        app_label = 'arko'
        verbose_name = "Região Intermediária"
        verbose_name_plural = "Regiões Intermediárias"
        db_table = f'{app_label}_RegiaoIntermediaria'
    def __str__(self):
        return self.nome

class RegiaoImediata(models.Model):
    id_ibge = models.IntegerField()
    nome = models.CharField(max_length=100)
    regiao_intermediaria = models.ForeignKey(RegiaoIntermediaria, on_delete=models.CASCADE, related_name="regioes_imediatas")
    class Meta:
        app_label = 'arko'
        verbose_name = "Região Imediata"
        verbose_name_plural = "Regiões Imediatas"
        db_table = f'{app_label}_RegiaoImediata'
    def __str__(self):
        return self.nome

class Municipio(models.Model):
    id_ibge = models.IntegerField()
    nome = models.CharField(max_length=100)
    microrregiao = models.ForeignKey(Microregiao, on_delete=models.CASCADE, related_name="municipios", null=True, blank=True)
    mesoregiao = models.ForeignKey(Mesoregiao, on_delete=models.CASCADE, related_name="municipios", null=True, blank=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, related_name="municipios")
    regiao_imediata = models.ForeignKey(RegiaoImediata, on_delete=models.CASCADE, related_name="municipios", null=True, blank=True)
    regiao_intermediaria = models.ForeignKey(RegiaoIntermediaria, on_delete=models.CASCADE, related_name="municipios", null=True, blank=True)
    class Meta:
        app_label = 'arko'
        verbose_name = "Município"
        verbose_name_plural = "Municípios"
        db_table = f'{app_label}_Municipio'
    def __str__(self):
        return self.nome


class Distrito(models.Model):
    id_ibge = models.IntegerField()
    nome = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name="distritos")
    class Meta:
        app_label = 'arko'
        verbose_name = "Distrito"
        verbose_name_plural = "Distritos"
        db_table = f'{app_label}_Distrito'
    def __str__(self):
        return self.nome