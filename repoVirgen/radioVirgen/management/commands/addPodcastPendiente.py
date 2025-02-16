import random
from django.core.management import BaseCommand
from radioVirgen.models import Usuario, Podcast, Programa, Reproduccion, LikePrograma, LikePodcast, ListaPodcastPendientes

class addPodcastPendientes(BaseCommand):
    help = 'Añadir podcasts pendientes a usuarios'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())
        programas = list(Programa.objects.all())

        if not usuarios or not programas:
            self.stdout.write(self.style.ERROR('No hay suficientes datos en la base de datos.'))
            return

        for _ in range(400):
            usuario = random.choice(usuarios)
            programa = random.choice(programas)
            ListaPodcastPendientes.objects.create(usuario=usuario, programa=programa)
        self.stdout.write(self.style.SUCCESS('Podcasts pendientes añadidos con éxito'))
