from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=150)
    age = models.PositiveSmallIntegerField('Edad')

    def __str__(self):
        return f'{self.name} {self.last_name}'