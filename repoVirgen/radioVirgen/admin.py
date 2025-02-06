from django.contrib import admin

from .models import Programa, Podcast, Autor, AutorPodcast, Usuario, Reproduccion, ListaPodcastPendientes, LikePrograma, LikePodcast

# Register your models here.
admin.site.register(Programa)
admin.site.register(Podcast)
admin.site.register(Autor)
admin.site.register(AutorPodcast)
admin.site.register(Usuario)
admin.site.register(Reproduccion)
admin.site.register(ListaPodcastPendientes)
admin.site.register(LikePrograma)
admin.site.register(LikePodcast)