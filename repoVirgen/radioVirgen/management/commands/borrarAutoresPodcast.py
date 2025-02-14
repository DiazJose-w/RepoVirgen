from django.core.management import BaseCommand

from radioVirgen.models import AutorPodcast


class Command(BaseCommand):
    help='Borrar asignaciones entre podcast y autores'

    def handle(self, *args, **kwargs):
        try:
            AutorPodcast.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Asignaciones borradas con éxito'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Hubo algún error al eliminar las asignaciones'))