from django.core.management import BaseCommand
from numpy.f2py.crackfortran import requiredpattern

from radioVirgen.models import Podcast, LikePodcast, Usuario, ListaPodcastPendientes


class Command(BaseCommand):
    help='Añadir me gusta a podcast. Listar los me gusta del usuario'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id',
            type= int,
            help='Id del usuario',
            required = False
        )

        parser.add_argument(
            '--nick',
            type=str,
            help='Nick del usuario',
            required= False
        )

        parser.add_argument(
            '--podcast',
            type=str,
            help='Nombre del podcast',
            required=False
        )

    def handle(self, *args, **kwargs):
        idUse = kwargs.get('id')
        nick = kwargs.get('nick')
        pod = kwargs.get('podcast')
        try:
            if not idUse:
                if not nick or not pod:
                    self.stdout.write(self.style.WARNING('Debes decirme nick de usuario y podcast para añadir un me gusta'))
                else:
                    #Con el nick y pod saco los id.
                    idUsuario = Usuario.objects.filter(nick=nick).first().id
                    idPodcast = Podcast.objects.filter(nombre= pod).first().id

                    listaLikes= LikePodcast.objects.all()
                    if idUsuario in listaLikes and idPodcast in listaLikes:
                        self.stdout.write(self.style.SUCCESS(f'El usuario {nick} ya tiene un like en este podcast {pod}'))
                    else:
                        nk = Usuario.objects.filter(nick=nick).first()
                        pd = Podcast.objects.filter(nombre=pod).first()
                        LikePodcast.objects.create(
                            usuario=nk,
                            podcast=pd
                        )
                        self.stdout.write(self.style.SUCCESS('Like añadido'))

            else:
                likeUser = LikePodcast.objects.filter(usuario=idUse)
                self.stdout.write(self.style.SUCCESS('hola muy buenas'))
                if likeUser.exists():
                    for like in likeUser:
                        self.stdout.write(self.style.SUCCESS(f'{like}'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error {e}'))