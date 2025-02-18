from django.core.management import BaseCommand

from radioVirgen.models import Usuario


class Command(BaseCommand):
    help='Mostrar todos los usuarios de la base de datos'

    def handle(self, *args, **kwargs):
        try:
            listaUsuarios =Usuario.objects.all()
            for i in listaUsuarios:
                self.stdout.write(self.style.SUCCESS(f'Nombre {i.nombre}. '
                                                     f'Apellidos {i.apellido}'
                                                     f'Nick {i.nick}. '
                                                     f'id {i.id}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al mostrar la lista de usuarios {e}'))