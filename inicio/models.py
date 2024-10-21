from django.db import models

# Create your models here.
 
class Libro(models.Model):
    nombre = models.CharField(max_length=30) 
    genero = models.CharField(max_length=30)
    autor = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nombre}'