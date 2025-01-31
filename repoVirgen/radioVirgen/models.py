from django.db import models
from django.db.models import Q


# Create your models here.

class Programa(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    descripcion = models.CharField(max_length=300)
    fecha_alta = models.DateField(null=True,blank=True)
    fecha_baja = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Programa ${self.nombre}'

class Podcast(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.CharField(max_length=300)
    categoria = models.CharField(max_length=50)
    fecha_alta = models.DateField(null=True, blank=True)
    fecha_baja = models.DateField(null=True, blank=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="episodios")
    link_drive = models.CharField(max_length=255)

    def __str__(self):
        return f'Podcast ${self.nombre}'

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(categoria__in=["Educativo", "Comedia", "Formación"]),
                name="check_categoria_values"
            )
        ]

class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=125)
    fecha_nac = models.DateField(null=True, blank=True)
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name="autores")

    def __str__(self):
        return f'Autor ${self.nombre} ${self.apellido}'

class AutorPodcast(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="podcasts")
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name="autores")

    def __str__(self):
        return f'Autor ${self.autor} hace podcast ${self.podcast}'

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nick = models.CharField(max_length=100, unique=True)
    fecha_nac = models.DateField(null=True, blank=True)

    def _str_(self):
        return f'Nombre: {self.nombre}\n Nick: {self.nick}'

class Reproduccion(models.Model):
    usuario= models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='podcast')

    def _str_(self):
        return f'Podcast ${self.podcast} reproducido por {self.usuario}'

class ListaPodcastPendientes(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='programa')

    def _str_(self):
        return f'Usuario {self.usuario}, progrma {self.programa}'

class LikePrograma(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, related_name='programa')

    def _str_(self):
        return f'Usuario {self.usuario} programa {self.programa}'


class LikePodcast(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='usuario')
    podcast = models.ForeignKey(Podcast, on_delete=models.CASCADE, related_name='podcast')

    def _str_(self):
        return f'Usuario {self.usuario} podcast {self.podcast}'