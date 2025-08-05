from django.db import models

# Create your models here.

class Mesoregiao(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.ForeignKey('Estados', on_delete=models.CASCADE, related_name='mesoregiao')
    class Meta:
        verbose_name = "Mesoregiao"
        verbose_name_plural = "Mesoregioes"
        db_table = f'{self._meta.app_label}_{self._meta.model_name}'
    def __str__(self):
        return self.nome


class Microregiao(models.Model):
    nome = models.CharField(max_length=100)
    


class Regiao(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Região"
        verbose_name_plural = "Regiões"
        db_table = f'{self._meta.app_label}_{self._meta.model_name}'
    def __str__(self):
        return self.nome

class Estados(models.Model):
    sigla = models.CharField(max_length=2)
    nome = models.CharField(max_length=100)
    regiao = models.OneToOneField(Regiao, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        dt_table = f'{self._meta.app_label}_{self._meta.model_name}'
    def __str__(self):
        return self.nome