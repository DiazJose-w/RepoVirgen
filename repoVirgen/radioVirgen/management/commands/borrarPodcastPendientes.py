from django.core.management import BaseCommand

from radioVirgen.models import ListaPodcastPendientes


class Command(BaseCommand):
    help='Borrar la lista de podcast pendientes'

    def handle(self, *args, **kwargs):
        try:
            ListaPodcastPendientes.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Lista borrada con éxito'))
        except Exception as e:
            self.stdout.write(self.style.SUCCESS(f'Error al borrar la lista {e}'))
