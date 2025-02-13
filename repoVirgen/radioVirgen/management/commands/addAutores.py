from faker import Faker
from django.core.management import BaseCommand
import random

from radioVirgen.models import Programa, Autor


class Command(BaseCommand):
    help='Añadir autores a la base de datos'

    def handle(self, *args, **kwargs):
        faker = Faker()
        programas = Programa.objects.all()

        try:
            if not Autor.objects.exists():
                for i in range(1, 31):
                    fechaNacimiento = faker.date_time_between(start_date='-65y', end_date='-18y')

                    Autor.objects.create(
                        nombre=faker.name(),
                        apellido=faker.last_name(),
                        fecha_nac=fechaNacimiento,
                        programa=random.choice(programas)
                    )
                    self.stdout.write(self.style.SUCCESS('Autor creado'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Hubo algún error al añadir los autores: {e}'))