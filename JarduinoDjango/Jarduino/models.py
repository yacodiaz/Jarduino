from django.db import models

# Create your models here.
class Planta(models.Model):
    def __str__(self):
        return self.genetica
    genetica = models.CharField(max_length = 200)
    puntuacion = models.IntegerField(default=0)
    fecha = models.DateField('dia plantada')

#class Carpa(models.Model):
