import random
from django.core.management import BaseCommand
from radioVirgen.models import Usuario, Podcast, Programa, Reproduccion, LikePrograma, LikePodcast, ListaPodcastPendientes

class Command(BaseCommand):
    help = 'Añadir likes de usuarios a podcasts'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())
        podcasts = list(Podcast.objects.all())

        if not usuarios or not podcasts:
            self.stdout.write(self.style.ERROR('No hay suficientes datos en la base de datos.'))
            return

        for _ in range(300):
            usuario = random.choice(usuarios)
            podcast = random.choice(podcasts)
            LikePodcast.objects.create(usuario=usuario, podcast=podcast)
        self.stdout.write(self.style.SUCCESS('Likes en podcasts añadidos con éxito'))