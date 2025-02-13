from django.core.management import BaseCommand

from radioVirgen.models import Autor


class Command(BaseCommand):
    help='Borrar autores'

    def handle(self, *args, **kwargs):
        try:
            Autor.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos los autores borrados con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('No se puedo borrar los autores'))