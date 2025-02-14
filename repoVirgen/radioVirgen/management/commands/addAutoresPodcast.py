import logging
import random

from django.core.management import BaseCommand

from radioVirgen.models import Autor, Podcast, AutorPodcast


class Command(BaseCommand):
    help = 'Asignar autores podcast'

    def handle(self, *args, **kwargs):
        autores = Autor.objects.all()
        podcast = Podcast.objects.all()

        try:
            for i in autores:
                AutorPodcast.objects.create(
                    autor=random.choice(autores),
                    podcast=random.choice(podcast)
                )
                self.stdout.write(self.style.SUCCESS(f'Autor añadido con éxito al podcast'))

            logging.info('que pasa aquí')
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Hubo algun error al asignar los autores al podcast: {e}'))