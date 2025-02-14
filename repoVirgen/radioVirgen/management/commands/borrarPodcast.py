from django.core.management import BaseCommand

from radioVirgen.models import Podcast


class Command(BaseCommand):
    help='Borrar todos los podcast'

    def handle(self, *args, **kwargs):
        try:
            Podcast.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Todos los podcasts borrados'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error al eliminar los podcast'))