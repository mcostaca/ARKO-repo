#*- coding: utf-8 -*-
import csv
import os
import pandas as pd
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from arko.models.empresas import Empresa

class Command(BaseCommand):
    help = 'Importa dados de empresas do CSV de dados abertos CNPJ'

    def handle(self, *args, **options):
        csv_path = os.path.join(settings.BASE_DIR, 'cnpj.EMPRECSV')

        if not os.path.exists(csv_path):
            raise CommandError(f'O arquivo "{csv_path}" não foi encontrado.')

        #estava fazendo uma iteração comum no csv porém o arquivo é muito grande e precisei de uma nova abordagem com pandas
        #limitando o numero de linhas em 200000 por que o csv original possui mais de 1800000, para facilitar a importação
        for chunk in pd.read_csv(csv_path,nrows=200000 ,sep=';', encoding='latin1', chunksize=100000):
            empresas = []
            for _, row in chunk.iterrows():
                empresa = Empresa(
                    cnpj_basico=row.iloc[0],
                    nome_razao_social=row.iloc[1],
                    natureza_juridica=row.iloc[2],
                    qualificacao_responsavel=row.iloc[3],
                    #transforma o capital em decimal
                    capital_social=row.iloc[4].replace(',','.'),
                    porte_empresa=row.iloc[5],
                    ente_federativo_responsavel=row.iloc[6] if row.iloc[6] else None
                    )
                empresas.append(empresa)
                self.stdout.write(self.style.SUCCESS(f'Empresa {empresa.nome_razao_social} adicionada à lista para importação.'))

            Empresa.objects.bulk_create(empresas, batch_size=5000)
