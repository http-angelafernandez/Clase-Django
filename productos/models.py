from django.db import models

# Create your models here.

class Cuento(models.Model):
    titulo = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.titulo}'
