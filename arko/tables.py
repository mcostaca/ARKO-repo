import django_tables2 as tables
from .models.localidades import Estado, Municipio, Distrito

class EstadoTable(tables.Table):
    class Meta:
        model = Estado
        template_name = "django_tables2/bootstrap.html"

class MunicipioTable(tables.Table):
    class Meta:
        model = Municipio
        template_name = "django_tables2/bootstrap.html"

class DistritoTable(tables.Table):
    class Meta:
        model = Distrito
        template_name = "django_tables2/bootstrap.html"
