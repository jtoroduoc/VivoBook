import uuid
from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse

# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=200, help_text='Ingrese el nombre del genero del libro (Ej. Ciencia Ficción)')

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', null=True, blank=True)
    fecha_muerte = models.DateField('Fecha de Fallecimiento', null=True, blank=True)

    class Meta:
        ordering = ['apellido', 'nombre']
    
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'

    def get_absolute_url(self):
        return reverse("autor-detalle", args=[str(self.id)])
    

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True)
    resumen = models.TextField(max_length=1000, help_text='Ingresa una breve descripción del libro')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 caracteres <a href="https://www.isbn-international.org/es/content/%C2%BFqu%C3%A9-es-un-isbn">número ISBN</a>')
    genero = models.ManyToManyField(Genero, help_text='Seleccione un genero para este libro')

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse("libro-detalle", args=[str(self.id)])

class Idioma(models.Model):
    nombre = models.CharField(max_length=50, help_text='Ingrese el idioma del libro (Ej. Español)')

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    ESTADO_PRESTAMO = (
        ('m', 'Mantenimiento'),
        ('p', 'Prestamo'),
        ('d', 'Disponible'),
        ('r', 'Reservado'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID único par este libro en particular en toda la bliblioteca')
    libro = models.ForeignKey(Libro, on_delete=models.SET_NULL, null=True)
    idioma = models.ForeignKey(Idioma, on_delete=models.SET_NULL, null=True)
    impreso = models.CharField(max_length=200)
    devolucion = models.DateField(null=True, blank=True)
    estatus = models.CharField(max_length=1, choices=ESTADO_PRESTAMO, blank=True, default='m', help_text='Disponibilidad de libro')

    class Meta:
        ordering: ['devolucion']
    
    def __str__(self):
        return f'{self.id (self.libro.titulo)}'