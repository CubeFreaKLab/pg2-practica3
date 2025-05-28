from rest_framework import serializers
from .models import Pelicula, Serie, Actor, Rol

class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelicula
        fields = [
            "id", 
            "titulo",
            "descripcion",
            "fecha_estreno",
            "duracion",
            "genero",
            "director",
        ]

class SerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serie
        fields = [
            "id",
            "titulo",
            "descripcion",
            "fecha_estreno",
            "temporadas",
            "episodios",
            "creador",
        ]

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            "id",
            "nombre",
            "fecha_nacimiento",
            "nacionalidad",
        ]

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = [
            "id",
            "actor",
            "pelicula",
            "serie",
            "nombre_personaje",
        ]
