from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'popula o DB com: contas de usuario, dados do IBGE e do CNPJ das empresas'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Iniciando o populatedb...'))
        self.stdout.write(self.style.SUCCESS('O Arquivo de CNPJS é muito grande, então tome um café enquanto isso :)'))
        call_command('makemigrations')
        call_command('migrate')
        admin = User.objects.create_superuser('rafael_admin', 'rafael@arko.com', 'admin123')
        user = User.objects.create_user(username='rafael_user',password='user123')
        call_command('importar_ibge_distritos')
        call_command('importar_empresas')
        
        self.stdout.write(self.style.SUCCESS('Banco populado'))