from django.core.management import BaseCommand

from radioVirgen.models import Podcast, LikePodcast


class Command(BaseCommand):
    help='Añadir me gusta a podcast. Listar los me gusta del usuario'
    def add_arguments(self, parser):
        #Añadimos arguemento de busqueda de usuario para añadirle el podcast pendiente
        parser.add_argument(
            '--id',
            type= int,
            help='Id del podcast',
            required = False
        )

    def handle(self, *args, **kwargs):
        idPoscast = kwargs.get('idPodcast')
        try:
            listPodcast = Podcast.objects.all()
            listLikePodcast = LikePodcast.objects.all()

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error {e}'))