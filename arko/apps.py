from django.apps import AppConfig


class ArkoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'arko'
    def ready(self):
        #como mudei os models e criei uma subpasta dentro do app, preciso esperar o  appconfig estar pronto para poder importar os models
        from .models.empresas import Empresa
        from .models.localidades import Regiao, Estado, Mesoregiao, Microregiao, Municipio, Distrito, RegiaoIntermediaria, RegiaoImediata, BaseModel