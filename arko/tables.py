import django_tables2 as tables
from .models.localidades import Estado, Municipio, Distrito
from .models.empresas import Empresa

#classe base evitar linhas de codigo repetidas
class BaseTable(tables.Table):
    class Meta:
        template_name = "django_tables2/bootstrap.html"

class EstadoTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Estado

class MunicipioTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Municipio
class DistritoTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Distrito

class EmpresaTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = Empresa