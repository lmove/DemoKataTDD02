from __future__ import unicode_literals

from django.db import models


# JD.RUNZA -060216:/Modelo Taller 1 Detalle en Drive


class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)


class Independiente(models.Model):
    id = models.AutoField(primary_key=True)
    idServicio = models.ForeignKey(Servicio)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    aniosExperiencia = models.IntegerField()
    foto = models.TextField()
    telefono = models.IntegerField()
    correoElectronico = models.EmailField(max_length=50, unique=True)
    contrasenia = models.CharField(max_length=15)
    fechaRegistro = models.DateTimeField(auto_now_add=True, blank=True)


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    idIdependiente = models.ForeignKey(Independiente)
    correoElectronico = models.CharField(max_length=50)
    texto = models.CharField(max_length=1000)
