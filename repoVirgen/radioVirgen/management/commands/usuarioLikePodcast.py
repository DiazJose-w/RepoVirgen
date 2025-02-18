from django.core.management.base import BaseCommand
from django.db.utils import DatabaseError, OperationalError
from radioVirgen.models import LikePodcast, Usuario, Podcast

class Command(BaseCommand):
    help = 'Permite a un usuario dar like a un podcast si no lo ha hecho antes y lista sus likes.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--pid',
            type=int,
            help='ID del podcast',
            required=True
        )
        parser.add_argument(
            '--uid',
            type=int,
            help='ID del usuario',
            required=True
        )

    def handle(self, *args, **kwargs):
        try:
            podcast_id = kwargs['pid']
            usuario_id = kwargs['uid']

            try:
                podcast = Podcast.objects.get(id=podcast_id)
            except Podcast.DoesNotExist:
                self.stderr.write("Error: No se encontró un podcast con ese ID.")
                return

            try:
                usuario = Usuario.objects.get(id=usuario_id)
            except Usuario.DoesNotExist:
                self.stderr.write("Error: No se encontró el usuario con ese ID.")
                return

            if LikePodcast.objects.filter(usuario=usuario, podcast=podcast).exists():
                self.stdout.write("El usuario ya ha dado like a este podcast.")
            else:
                LikePodcast.objects.create(usuario=usuario, podcast=podcast)
                self.stdout.write(f"Like agregado al podcast '{podcast.nombre}' por {usuario.nombre}.")

            # Listar todos los podcasts a los que el usuario ha dado like
            likes = LikePodcast.objects.filter(usuario=usuario)
            self.stdout.write(f"\nPodcasts que le gustan a {usuario.nombre}:")
            for like in likes:
                self.stdout.write(f"- {like.podcast.nombre}")

        except (DatabaseError, OperationalError) as db_error:
            self.stderr.write(f"Error en la base de datos: {db_error}")
        except Exception as e:
            self.stderr.write(f"Error inesperado: {e}")
