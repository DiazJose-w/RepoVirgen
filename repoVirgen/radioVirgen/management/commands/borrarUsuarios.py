from django.core.management import BaseCommand
from django.utils.autoreload import ensure_echo_on

from radioVirgen.models import Usuario


class Command(BaseCommand):
    help='Borrar usuarios'

    def handle(self, *args, **kwargs):
        try:
            Usuario.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Borrados con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Hubo un error en el borrado'))