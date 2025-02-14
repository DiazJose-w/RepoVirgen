from django.core.management import BaseCommand
from faker import Faker

from radioVirgen.models import Usuario

class Command(BaseCommand):
    help = 'Crear usuarios'

    def handle(self, *args, **kwargs):
        faker = Faker()
        try:
            for i in range(1, 11):
                fechaNacimiento = faker.date_time_between(start_date='-65y', end_date='-18y')
                Usuario.objects.create(
                    nombre=faker.name(),
                    apellido=faker.last_name(),
                    nick=faker.name(),
                    fecha_nac=fechaNacimiento
                )
                self.stdout.write(self.style.SUCCESS(f'usuario añadido con éxito'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Hubo un error al añadir a los usuarios {e}'))