from django.contrib import admin
from .models import Autor, Genero, Libro, Idioma, Inventario

# Register your models here.
admin.site.register(Idioma)
admin.site.register(Genero)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'fecha_nacimiento', 'fecha_muerte')
    fields = [('nombre', 'apellido'), 'fecha_nacimiento', 'fecha_muerte']

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_filter = ('estatus', 'devolucion')
    fieldsets = (
        ('Libro', {
            'fields': ('libro', 'impreso', 'idioma', 'id')
        }),
        ('Disponibilidad', {
            'fields': ('estatus', 'devolucion')
        })
    )

