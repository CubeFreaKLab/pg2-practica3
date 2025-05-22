from django.db import models

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    genero = models.CharField(max_length=50)
    director = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Serie(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_estreno = models.DateField()
    temporadas = models.PositiveIntegerField()
    episodios = models.PositiveIntegerField()
    creador = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

class Actor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Rol(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, blank=True, null=True)
    serie = models.ForeignKey(Serie, on_delete=models.CASCADE, blank=True, null=True)
    nombre_personaje = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre_personaje} - {self.actor.nombre}"
