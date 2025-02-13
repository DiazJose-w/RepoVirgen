from django.core.management import BaseCommand
from radioVirgen.models import Programa

class Command(BaseCommand):
    help='Borrar todos los programas'

    def handle(self, *args, **kwargs):
        try:
            Programa.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Programas borrados con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Hubo un error en el borrado de los programas'))