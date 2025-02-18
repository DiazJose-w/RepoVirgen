from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError, OperationalError
from radioVirgen.models import ListaPodcastPendientes, Usuario, Podcast

class Command(BaseCommand):
    help = 'Añadir un podcast a la lista de pendientes de un usuario y puede pasarse o nombre o ID de usuario'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pid',
            type=int,
            help='ID del podcast a añadir',
            required=True
        )
        parser.add_argument(
            '--uid',
            type=int,
            help='ID del usuario'
        )
        parser.add_argument(
            '--nom',
            type=str,
            help='Nombre del usuario'
        )

    def handle(self, *args, **kwargs):
        try:
            podcast_id = kwargs['pid']
            usuario_id = kwargs['uid']
            nombre = kwargs['nom']

            if usuario_id and nombre:
                self.stderr.write("Error: No puedes proporcionar tanto el ID como el Nick del usuario. Usa solo uno")
                return

            try:
                podcast = Podcast.objects.get(id=podcast_id)
            except Podcast.DoesNotExist:
                self.stderr.write(f"Error: No se encontró un podcast con ese ID")
                return

            try:
                if usuario_id:
                    usuario = Usuario.objects.get(id=usuario_id)
                elif nombre:
                    usuario = Usuario.objects.get(nombre=nombre)
                else:
                    self.stderr.write("Error: Debes proporcionar un ID de usuario o un nombre.")
                    return
            except Usuario.DoesNotExist:
                self.stderr.write("Error: No se encontró el usuario")
                return

            if ListaPodcastPendientes.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write("El podcast ya está en la lista de pendientes del usuario")
                return

            ListaPodcastPendientes.objects.create(usuario=usuario, podcast=podcast)
            self.stdout.write(f"Podcast '{podcast.nombre}' añadido a la lista de pendientes de {usuario.nombre} ({usuario.nick}).")

        except (DatabaseError, OperationalError) as db_error:
            self.stderr.write(f"Error en la base de datos: {db_error}")
        except Exception as e:
            self.stderr.write(f"Error inesperado: {e}")
