[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2%2B-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)](https://jquery.com/)
[![Poetry](https://img.shields.io/badge/Poetry-60A5FA?style=for-the-badge&logo=poetry&logoColor=white)](https://python-poetry.org/)


# [ARKOAPP]

Teste tecnico para a empresa ARKO, listando dados importados via API do ibge e csv com os dados abertos dos CNPJ.

### Instalando dependencias

**Clone o repositório**
    ```
$ git clone https://github.com/mcostaca/ARKO-repo
    ```

**Instale o poetry globalmente**
    ```
$ curl -sSL https://install.python-poetry.org | python3 -
    ```

**crie a venv com o poetry**

    ```
    $ poetry env activate

    ```

Esse comando cria o ambiente e retorna o comando para ativar a venv source /path....

**Instale as dependencias com o poetry**
    ```
$ poetry install
    ```

### ⚙️ Configuração

**Variáveis de Ambiente:**
    crie um .env e preencha com as informações do seu DB

    ```
    DB_NAME=...
    DB_USER=...
    DB_PASSWORD=...
    DB_HOST=...
    DB_PORT=...
    ```

**Execute o command padrão para criar e popular as tabelas**
    ```$
    python manage.py populatedb
    ```
    É importante baixar e mover o csv do cnpj para a pasta raiz com o nome: cnpj.EMPRECSV