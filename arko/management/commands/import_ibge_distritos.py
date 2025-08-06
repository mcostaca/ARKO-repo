import requests
from django.core.management.base import BaseCommand
from arko.models import Regiao, Estado, Mesoregiao, Microregiao, Municipio, Distrito, RegiaoIntermediaria, RegiaoImediata

class Command(BaseCommand):
    help = 'Importa dados do endpoint do IBGE e persiste na base default.'

    def handle(self, *args, **options):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
        response = requests.get(url)
        data = response.json()
        #um print estilizado apenas para guiar o começo do script
        self.stdout.write(self.style.SUCCESS('Importação iniciada'))

        for distrito in data:
            municipio_data = distrito.get('municipio') or {}
            micro_data = municipio_data.get('microrregiao') or {}
            meso_data = micro_data.get('mesorregiao') or {}
            estado_data = meso_data.get('UF') or {}
            regiao_data = estado_data.get('regiao') or {}

            # path caso não haja microrregiao buscar via regiao-intermediaria['UF']
            regiao_imediata_data = municipio_data.get('regiao-imediata') or {}
            regiao_intermediaria_data = regiao_imediata_data.get('regiao-intermediaria') or {}
            uf_temp = regiao_intermediaria_data.get('UF') if regiao_intermediaria_data else None
            if not estado_data and uf_temp:
                estado_data = uf_temp or {}
                regiao_data = estado_data.get('regiao') or {}
            # path caso não houver mesorregiao buscar via uf_temp
            meso_fallback = None
            if not meso_data and uf_temp:
                meso_fallback = {'id': None, 'nome': '', 'UF': estado_data}
                meso_data = meso_fallback
            # se não houver microrregiao, criar dummy
            if not micro_data and meso_data:
                micro_data = {'id': None, 'nome': '', 'mesorregiao': meso_data}

            if regiao_data:
                regiao, _ = Regiao.objects.get_or_create(
                    id_ibge=regiao_data.get('id'),
                    sigla=regiao_data.get('sigla', ''),
                    nome=regiao_data.get('nome', '')
                )
            if estado_data:
                estado, _ = Estado.objects.get_or_create(
                    id_ibge=estado_data.get('id'),
                    sigla=estado_data.get('sigla', ''),
                    nome=estado_data.get('nome', ''),
                    regiao=regiao
                )
            if meso_data and meso_data.get('id') is not None:
                mesoregiao, _ = Mesoregiao.objects.get_or_create(
                    id_ibge=meso_data.get('id'),
                    nome=meso_data.get('nome', ''),
                    estado=estado
                )
            
            if micro_data and micro_data.get('id') is not None:
                microregiao, _ = Microregiao.objects.get_or_create(
                    id_ibge=micro_data.get('id'),
                    nome=micro_data.get('nome', ''),
                    mesoregiao=mesoregiao
                )
            regiao_imediata_data = municipio_data.get('regiao-imediata') or {}
            regiao_intermediaria_data = regiao_imediata_data.get('regiao-intermediaria') or {}
            if regiao_intermediaria_data:
                regiao_intermediaria, _ = RegiaoIntermediaria.objects.get_or_create(
                    id_ibge=regiao_intermediaria_data.get('id'),
                    nome=regiao_intermediaria_data.get('nome', ''),
                    estado=estado
                )
            if regiao_imediata_data:
                regiao_imediata, _ = RegiaoImediata.objects.get_or_create(
                    id_ibge=regiao_imediata_data.get('id'),
                    nome=regiao_imediata_data.get('nome', ''),
                    regiao_intermediaria=regiao_intermediaria
                )
            try:
                if municipio_data:
                    municipio, _ = Municipio.objects.get_or_create(
                        id_ibge=municipio_data.get('id'),
                        nome=municipio_data.get('nome', ''),
                        microrregiao=microregiao,
                        mesoregiao=mesoregiao,
                        estado=estado,
                        regiao_imediata=regiao_imediata,
                        regiao_intermediaria=regiao_intermediaria
                    )
                Distrito.objects.get_or_create(
                    id_ibge=distrito.get('id'),
                    nome=distrito.get('nome', ''),
                    municipio=municipio
                )
            except Exception as e:
                #mensagem com JSON caso erro
                 self.stdout.write(self.style.WARNING('Erro ao persistir uma resposta', distrito))
        #mensagem fim do script
        self.stdout.write(self.style.SUCCESS('Importação concluída!'))        