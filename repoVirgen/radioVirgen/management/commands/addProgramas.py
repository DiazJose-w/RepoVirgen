from datetime import timedelta
from random import Random, random

from django.core.management import BaseCommand
from faker.proxy import Faker

from repoVirgen.radioVirgen.models import Programa


class Command(BaseCommand):
    help= 'Añadir programas a la base de datos'

    def handle(self, *args, **kwargs):
        faker = Faker()

        if not Programa.objects.exists():
            for i in range(1, 300):
                fecha_aleatoria = faker.date_time_between(start_date='-5y', end_date='now')
                if random.random() < 0.5:  # 50% de probabilidad de tener fecha de baja
                    fecha_ale_baja = fecha_aleatoria + timedelta(
                        days=random.randint(30, 365 * 5))  # Mínimo 1 mes después, máximo 5 años después
                else:
                    fecha_ale_baja = None

                fecha_formateada = fecha_aleatoria.strftime('%Y-%,-%d')

                Programa.objects.create(nombre = faker.sentence(nb_words=3),
                                        descripcion = faker.sentence(nb_words= 10),
                                        fecha_alta = fecha_formateada,
                                        fecha_baja = fecha_ale_baja)
                self.stdout.write(self.style.SUCCESS('Programa añadido con éxito'))
        else:
            self.stderr.write(self.style.ERROR('Algo ha fallado en la inserción'))
