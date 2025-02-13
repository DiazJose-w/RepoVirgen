from datetime import timedelta

from django.core.management import BaseCommand
from faker import Faker
import random

from radioVirgen.models import Podcast, Programa


class Command(BaseCommand):
    help= 'Añadir programas a la base de datos'

    def handle(self, *args, **kwargs):
        faker = Faker()
        probabilidad = random.random()

        try:
            if not Podcast.objects.exists():
                for i in range(1, 300):
                    programas= Programa.objects.all()

                    fecha_aleatoria = faker.date_time_between(start_date='-5y', end_date='now')
                    if probabilidad < 0.5:
                        fecha_ale_baja = fecha_aleatoria + timedelta(
                            days=random.randint(30, 365 * 5))  # Mínimo 1 mes después, máximo 5 años después
                    else:
                        fecha_ale_baja = None

                    fecha_formateada = fecha_aleatoria.strftime('%Y-%m-%d')

                    Podcast.objects.create(nombre=faker.sentence(nb_words=3),
                                           descripcion=faker.sentence(nb_words=10),
                                           fecha_alta=fecha_formateada,
                                           fecha_baja=fecha_ale_baja,
                                           programa=random.choice(programas),
                                           #Pensar como añadir el linkDrive
                                           )
                    self.stdout.write(self.style.SUCCESS('Podcast añadido con éxito'))
            else:
                self.stderr.write(self.style.ERROR('Algo ha fallado en la inserción'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
