from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=150)
    age = models.PositiveSmallIntegerField('Edad')

    def __str__(self):
        return f'{self.name} {self.last_name}'
    

class Book(models.Model):
    title = models.CharField('Título',
        max_length= 250,
        unique= True
    )
    cu = models.CharField('Código único',
        max_length=15,
        unique=True
    )
        #author = models.OneToOneField(Author, on_delete=models.SET_NULL, null= True)
        #author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    author = models.ManyToManyField(Author)

    class Meta:
        verbose_name = 'Book',
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title
    
    #1. OBTENER TODOS LOS REGISTRO DE UNA TABLA 

Author.objects.all()

#SELECT "core_author"."id", 
# "core_author"."name", "core_author"."last_name", 
# "core_author"."age" FROM "core_author"

#2. OBTENER TODOS LOS AUTORES QUE TENGAN EN SU APELLIDO sea FLORES'

Author.objects.filter(last_name='Flores').first()

#3.