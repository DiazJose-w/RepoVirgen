import random
from django.core.management import BaseCommand
from radioVirgen.models import Usuario, Podcast, Programa, Reproduccion, LikePrograma, LikePodcast, ListaPodcastPendientes

class Command(BaseCommand):
    help = 'Añadir podcasts pendientes a usuarios'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())
        listPodcast = list(Podcast.objects.all())

        if not usuarios or not listPodcast:
            self.stdout.write(self.style.ERROR('No hay suficientes datos en la base de datos.'))
            return

        for _ in range(400):
            usuario = random.choice(usuarios)
            podcast = random.choice(listPodcast)
            ListaPodcastPendientes.objects.create(usuario=usuario, podcast=podcast)
        self.stdout.write(self.style.SUCCESS('Podcasts pendientes añadidos con éxito'))
