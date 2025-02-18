import random
from django.core.management import BaseCommand
from radioVirgen.models import Usuario, Podcast, Programa, Reproduccion, LikePrograma, LikePodcast

class Command(BaseCommand):
    help = 'Añadir likes de usuarios a programas'

    def handle(self, *args, **kwargs):
        usuarios = list(Usuario.objects.all())
        programas = list(Programa.objects.all())

        if not usuarios or not programas:
            self.stdout.write(self.style.ERROR('No hay suficientes datos en la base de datos.'))
            return

        for _ in range(300):
            usuario = random.choice(usuarios)
            programa = random.choice(programas)
            LikePrograma.objects.create(usuario=usuario, programa=programa)
        self.stdout.write(self.style.SUCCESS('Likes en programas añadidos con éxito'))