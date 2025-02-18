from cgitb import handler
from datetime import datetime

from django.core.management import BaseCommand

from radioVirgen.models import Usuario


class Command(BaseCommand):
    help='Añadir usuario por parámetro'

    def add_arguments(self, parser):
        parser.add_argument(
            '--nombre',
            type= str,
            help='Nombre del nuevo usuario',
            required=False
        )

        parser.add_argument(
            '--apellido',
            type=str,
            help='Apellido del nuevo usuario',
            required=False
        )
        parser.add_argument(
            '--nick',
            type=str,
            help='Nick del nuevo usuario',
            required=False
        )
        parser.add_argument(
            '--fechaNacimiento',
            type=str,
            help='Fecha de nacimiento del nuevo usuario',
            required=False
        )

    def handle(self, *args, **kwargs):
        try:
            name = kwargs.get('nombre')
            lastName = kwargs.get('apellido')
            nick = kwargs.get('nick')
            date = kwargs.get('fechaNacimiento')

            if date:
                try:
                    date = datetime.strptime(date, '%d/%m/%Y').date()
                    self.stdout.write(self.style.SUCCESS(f'Fecha convertida: {date}'))
                except ValueError:
                    self.stdout.write(self.style.ERROR('Formato no válido, debe ser DD/MM/YYYY'))
            else:
                self.stdout.write(self.style.WARNING('Fecha de nacimiento no proporcionada'))


            if not name or not lastName or not nick or not date:
                self.stdout.write(self.style.WARNING('Debes añadir todos los datos'))
            else:
                nk = Usuario.objects.filter(nick=nick).first()
                if not nk:
                    Usuario.objects.create(
                        nombre=name,
                        apellido=lastName,
                        nick=nick,
                        fecha_nac=date
                    )
                    self.stdout.write(self.style.SUCCESS(f'Usuario {nick} creado con éxito'))
                else:
                    self.stdout.write(self.style.WARNING('El usuario ya existe'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error al crear usuario {e}'))













