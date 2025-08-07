from django.db import models
app_label = 'arko'

class Empresa(models.Model):

    cnpj_basico = models.CharField(max_length=8)
    nome_razao_social = models.CharField(max_length=255)
    natureza_juridica = models.CharField(max_length=4)
    qualificacao_responsavel = models.CharField(max_length=2)
    capital_social = models.DecimalField(max_digits=20, decimal_places=2)
    porte_empresa = models.CharField(max_length=2)
    ente_federativo_responsavel = models.CharField(max_length=2, null=True, blank=True)
    #no CSV apenas possuia os campos acima, então decidi não utilizar todos os campos
    '''
    cnpj_ordem
    cnpj_dv
    identificador_matriz_filial
    nome_fantasia
    situacao_cadastral
    data_situacao_cadastral
    motivo_situacao_cadastral
    nome_cidade_exterior
    pais
    cnpj
    ente_federativo_responsavel
    logradouro
    numero
    complemento
    bairro
    cep
    uf
    municipio
    ddd_telefone_1
    telefone_1
    ddd_telefone_2
    telefone_2
    ddd_fax
    fax
    email
    cnae_fiscal_principal
    cnae_fiscal_secundario
    data_abertura
    data_inicio_atividade
    situacao_especial
    data_situacao_especial
    '''
    class Meta:
        db_table = f'{app_label}_Empresa'
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        permissions = [
            ("pode_visualizar_dados_sensiveis", "Pode visualizar dados sensíveis de empresas"),
        ]

    def __str__(self):
        return f"{self.nome_razao_social} ({self.cnpj})"