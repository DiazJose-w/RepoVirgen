from django.core.management import BaseCommand

from radioVirgen.models import Usuario, Podcast, ListaPodcastPendientes


class Command(BaseCommand):
    help= 'Añade un podcast a la lista de pendientes a un usuario'

    def add_arguments(self, parser):
        #Añadimos arguemento de busqueda de usuario para añadirle el podcast pendiente
        parser.add_argument(
            '--nick',
            type= str,
            help='Nick del usuario',
            required = False
        )
        parser.add_argument(
            '--podcast',
            type=str,
            help='Poscast',
            required=False
        )

    def handle(self, *args, **kwargs):
        nick = kwargs.get('nick')
        pod = kwargs.get('podcast')

        try:
            usuario = Usuario.objects.filter(nick=nick)
            podcast = Podcast.objects.filter(nombre=pod)
            if not nick or not pod:
                self.stdout.write(self.style.WARNING('Debes indicar nick y podcast'))
            else:
                if not usuario.exists():
                    self.stdout.write(self.style.WARNING('Usuario no encontrado'))
                elif not podcast.exists():
                    self.stdout.write(self.style.WARNING('Podcast no encontrado'))
                else:
                    idUsuario = usuario.first()
                    idPodcast = podcast.first()
                    pend= ListaPodcastPendientes.objects.filter(usuario=idUsuario, podcast=idPodcast)
                    if not pend.exists():
                        try:
                            ListaPodcastPendientes.objects.create(
                                usuario=idUsuario,
                                podcast=idPodcast
                            )
                            self.stdout.write(self.style.SUCCESS(f'Poscast añadido a la lista de pendientes'))
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f'Error al añadir el podcast en la lista de pendientes {e}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'ya está en la lista de pendientes'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error en la búsqueda: {e}'))
