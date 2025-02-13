from django.core.management import BaseCommand
from numpy.ma.core import count

from radioVirgen.models import Programa

class Command(BaseCommand):
    help = 'Programas sin fecha de baja'

    def handle(self, *args, **kwargs):

        try:
            programasFinalizado = Programa.objects.filter(fecha_baja=None)

            for prom in programasFinalizado:
                self.stdout.write(self.style.SUCCESS(f'Programa: {prom}.'))

            print(f'Num {count(programasFinalizado)}')
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error en la busqueda'))