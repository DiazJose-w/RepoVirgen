import datetime
from datetime import datetime, timedelta
import random
from django.core.management import BaseCommand
from faker import Faker

from radioVirgen.models import Programa

class Command(BaseCommand):
    help= 'Añadir programas a la base de datos'

    def handle(self, *args, **kwargs):
        faker = Faker()
        try:
            if not Programa.objects.exists():
                for i in range(1, 301):
                    fecha_aleatoria = faker.date_time_between(start_date='-5y', end_date='now')
                    probabilidad = random.randint(1, 2)

                    if probabilidad == 1:
                        fecha_ale_baja = (fecha_aleatoria +
                                          timedelta(days=random.randint(30, 365 * 5)))

                        if fecha_ale_baja > datetime.now():
                            fecha_ale_baja =  None
                    else:
                        fecha_ale_baja = None

                    fecha_formateada = fecha_aleatoria.strftime('%Y-%m-%d')

                    Programa.objects.create(nombre=faker.sentence(nb_words=3),
                                            descripcion=faker.sentence(nb_words=10),
                                            fecha_alta=fecha_formateada,
                                            fecha_baja=fecha_ale_baja)
                    self.stdout.write(self.style.SUCCESS('Programa añadido con éxito'))
            else:
                self.stderr.write(self.style.ERROR('Algo ha fallado en la inserción'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
