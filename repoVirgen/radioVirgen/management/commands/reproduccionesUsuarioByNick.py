from django.core.management.base import BaseCommand
from repoVirgen.radioVirgen.models import *
from django.db.utils import DatabaseError, OperationalError


class Command(BaseCommand):
    help = 'Buscar reproducciones de usuario por nick'

    def handle(self, *args, **kwargs):
        try:
            if not args:
                self.stderr.write("Error: Debes proporcionar un nick.")
                return

            nick = args[0]

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

        except IndexError:
            self.stderr.write("Error: No se proporcionó un argumento para el nick.")
        except Exception as e:
            self.stderr.write(f"Error inesperado: {e}")
