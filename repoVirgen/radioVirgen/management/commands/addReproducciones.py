import random
from django.core.management import BaseCommand
from radioVirgen.models import Usuario, Podcast, Programa, Reproduccion, LikePrograma, LikePodcast, ListaPodcastPendientes

class Command(BaseCommand):
    help = 'Añadir reproducciones de usuarios en podcasts'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())
        podcasts = list(Podcast.objects.all())

        if not usuarios or not podcasts:
            self.stdout.write(self.style.ERROR('No hay suficientes datos en la base de datos.'))
            return

        for _ in range(500):
            usuario = random.choice(usuarios)
            podcast = random.choice(podcasts)
            Reproduccion.objects.create(usuario=usuario, podcast=podcast)
        self.stdout.write(self.style.SUCCESS('Reproducciones añadidas con éxito'))
