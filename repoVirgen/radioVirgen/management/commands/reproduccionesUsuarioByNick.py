from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError, OperationalError

from radioVirgen.models import Reproduccion


class Command(BaseCommand):
    help = 'Buscar reproducciones de usuario por nick'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nick',
            type=str,
            help='Nick para buscar reproducciones',
            required=True
        )

    def handle(self, *args, **kwargs):
        try:
            nick = kwargs['nick']

            try:
                reproducciones = Reproduccion.objects.all()
            except (DatabaseError, OperationalError) as db_error:
                self.stderr.write(f"Error en la base de datos: {db_error}")
                return

            encontrado = False
            for reproduccion in reproducciones:
                try:
                    if reproduccion.usuario and reproduccion.usuario.nick == nick:
                        self.stdout.write(f'{reproduccion}')
                        encontrado = True
                except AttributeError:
                    self.stderr.write("Advertencia: Una reproducción tiene un usuario inválido.")

            if not encontrado:
                self.stdout.write(f"No se encontraron reproducciones para el usuario '{nick}'.")


        except Exception as e:
            self.stderr.write(f"Error inesperado: {e}")
