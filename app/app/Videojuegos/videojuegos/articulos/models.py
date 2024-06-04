from django.db import models

GENERO = [
    ('1', 'Picudo de espina'),
    ('2', 'Chinche roja'),
    ('3', 'Picudo barrenador'),
]



class Articulos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    stock = models.IntegerField(default=0, null=True)
    genero = models.CharField('Genero', max_length=1, choices=GENERO)
    categoria = models.ForeignKey("articulos.Categoria", verbose_name='Categoria', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField('Descripcion', null=True, blank=True )

    def __str__(self):
        return self.nombre
